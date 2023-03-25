import numpy as np

class Team:
    def __init__(self, name, color_home, tackles_home, tackles_away,
                                    completions_home, completions_away):
        self.name = name

        self.color_home = color_home
        self.color_away = np.array([1.,1.,1.])
        self.color_field = np.array([96,185,34]) / 255 # So called 'Field Green'

        self.tackles_home = tackles_home
        self.tackles_away = tackles_away

        self.completions_home = completions_home
        self.completions_away = completions_away

        self.throws_home = None
        self.throws_away = None

    def relative_luminance(self, color):
        """the relative brightness of any point in a colorspace,
            normalized to 0 for darkest black and 1 for lightest white
            defined in https://www.w3.org/TR/2008/REC-WCAG20-20081211/#relativeluminancedef
        Args:
          color (arr): numpy array of color in sRGB format

        Returns:
          rel_lum: relative_luminance
        """
        Rs, Gs, Bs = color

        modify = lambda c : ((c + 0.055) / 1.055)**2.4

        # normalize R
        if Rs <= 0.03928:
            R = Rs / 12.92
        else:
            R = modify(Rs)

        # normalize G
        if Gs <= 0.03928:
            G = Gs / 12.92
        else:
            G = modify(Gs)

        # normalize B
        if Bs <= 0.03928:
            B = Bs / 12.92
        else:
            B = modify(Bs)

        L = 0.2126 * R + 0.7152 * G + 0.0722 * B

        return L

    def contrast(self, color1, color2=None):
        if color2 is None:
            color2 = self.color_field
            # print('setting color to field color...')
        L1 = self.relative_luminance(color1)
        L2 = self.relative_luminance(color2)

        if L2 > L1:
            contrast = (L2 + 0.05) / (L1 + 0.05)

        else:
            contrast = (L1 + 0.05) / (L2 + 0.05)

        return contrast

    def biserial_correlation(self, x, y):
        x_diff = x - np.mean(x)
        y_diff = y - np.mean(y)

        r_num = np.sum(x_diff * y_diff)
        r_denom = np.sqrt(np.sum((x_diff * y_diff)**2) * np.sum((x_diff * y_diff)**2))
        r = r_num / r_denom

        return r

    def corr_stderr(r, N):
        var = (1 - r**2) / (N - 2)

        return np.sqrt(var)

def main():
    pass

if __name__ == "__main__":
  main()
