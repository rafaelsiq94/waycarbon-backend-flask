class TcoFormat:
    @classmethod
    def convert_tco(self, tco):
        return format(tco, ".3f").replace(".", ",")
