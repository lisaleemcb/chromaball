class Team:
    def __init__(self, name, color_home, color_away):
        self.name = name

        self.color_home = None
        self.color_away = None
        self.color_field = None

        self.tackles_home = None
        self.tackles_away = None

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
        L = 0.2126 * R + 0.7152 * G + 0.0722 * B

        return L

    def contrast(self):
        L1 = relative_luminance(self.color_home)
        L2 = relative_luminance(self.color_field)

        contrast = (L1 + 0.05) / (L2 + 0.05)

        return contrast

    def pearson_correlation(self, x=None, y=None):
        if x == None
        x_diff = x - np.mean(x)
        y_diff = y - np.mean(y)

        r_num = np.sum(x_diff * y_diff)
        r_denom = np.sqrt(np.sum((x_diff * y_diff)**2) * np.sum((x_diff * y_diff)**2))
        r = r_num / r_denom

        return r

def main():
    pass

if __name__ == "__main__":
  main()
