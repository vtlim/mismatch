text_lhs = 'ATCG'
text_rhs = 'CGAA'


def reverse_complement(sequence):
    """
    """
    base_orig = ("U", "A", "T", "C", "G", "X", "Y")
    base_rev = ("T", "X", "A", "Y", "C", "T", "G")
    revcomp = sequence[::-1]
    for orig, rev in zip(base_orig, base_rev):
        revcomp = revcomp.replace(orig, rev)
    return revcomp

def locate_difference(text1, text2):
    """
    """
    # https://stackoverflow.com/a/8545568
    where_diff = [i for i in range(len(text1)) if text1[i] != text2[i]]
    return where_diff

print(text_lhs)
print(text_rhs)
print()
print(reverse_complement(text_rhs))
print(locate_difference(text_lhs, reverse_complement(text_rhs)))

print(locate_difference('Paste one version of a text here.', 'Paste another version of the text here.'))
