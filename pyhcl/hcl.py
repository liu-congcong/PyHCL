from math import cos, pi, pow, sin


class HCL:

    def __init__(self, type = 'hex', min_hue = 15.0, max_hue = 375.0, chroma = 100.0, luminance = 65.0):
        assert type in ('hex', 'dec'), 'valid "type" should be "hex" or "dec".'
        assert luminance > 0.0, '"luminance" should be a positive float.'

        self.type = type
        self.min_hue = min_hue
        self.max_hue = max_hue
        self.chroma = chroma
        self.luminance = luminance
        self.white_x = 95.047
        self.white_y = 100.0
        self.white_z = 108.883
        self.gamma = 2.4
        self.eps = 216.0 / 24389.0 # 0.008856452 #
        self.kappa = 24389.0 / 27.0 # 903.2963 #
        self.dec2hex = '0123456789ABCDEF'
        return None


    def xyz2rgb(self, x, y, z):
        for coefficient in (
            (3.2404542, -1.5371385, -0.4985314),
            (-0.9692660, 1.8760108, 0.0415560),
            (0.0556434, -0.2040259, 1.0572252)
        ):
            rgb = x * coefficient[0] + y * coefficient[1] + z * coefficient[2]
            rgb = 255.0 * (1.055 * pow(rgb, (1.0 / self.gamma)) - 0.055 if rgb > 0.0031308 else 12.92 * rgb)
            yield min(max(round(rgb), 0), 255)
        return None


    def output_color(self, r, g, b):
        if self.type == 'hex':
            color = '#' \
            + self.dec2hex[(r >> 4) & 15] + self.dec2hex[r & 15] \
            + self.dec2hex[(g >> 4) & 15] + self.dec2hex[g & 15] \
            + self.dec2hex[(b >> 4) & 15] + self.dec2hex[b & 15]
        elif self.type == 'dec':
            color = (r, g, b)
        return color


    def main(self, colors):
        assert colors > 0, '"colors" should be a positive integer.'

        white_1x_15y_3z = self.white_x + 15 * self.white_y + 3 * self.white_z
        u = 4.0 * self.white_x / white_1x_15y_3z
        v = 9.0 * self.white_y / white_1x_15y_3z
        Y = pow((self.luminance + 16.0) / 116.0, 3) if (self.luminance > self.eps * self.kappa) else self.luminance / self.kappa
        B = - 5.0 * Y
        if not (self.max_hue - self.min_hue) % 360:
            self.max_hue -= 360.0 / colors
        hue_step = (self.max_hue - self.min_hue) / (colors - 1.0) if colors > 1 else 0
        for color_index in range(colors):
            hue = min(max(self.min_hue + color_index * hue_step, 0), 360) * pi / 180.0
            A = 1.0 / 3.0 * (52.0 * self.luminance / (self.chroma * cos(hue) + 13.0 * self.luminance * u) - 1.0)
            X = (Y * (39.0 * self.luminance / (self.chroma * sin(hue) + 13.0 * self.luminance * v) - 5.0) - B) / (A + 1.0 / 3.0)
            Z = X * A + B
            yield self.output_color(*self.xyz2rgb(X, Y, Z))
        return self
