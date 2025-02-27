""""""

""" SABERMETRICS """

def obp(h, bb, hbp, ab, sf):
    '''
    Calculate On-Base Percentage (OBP) = (H + BB + HBP) / (AB + BB + HBP + SF)
    :param h: Hits.
    :param bb: Walks (Bases on Balls).
    :param hbp: Hit by Pitch.
    :param ab: At Bat.
    :param sf: Sacrifice Flies.
    :return:
    '''
    return (h + bb + hbp) / (ab + bb + hbp + sf)


## Definitely double check the remaining functions... ##


def slg(h, _2b, _3b, hr, ab):
    '''
    Calculate Slugging Percentage (SLG) = (1B + 2 * 2B + 3 * 3B + 4 * HR) / AB
    :param h: Hits.
    :param _2b: Doubles.
    :param _3b: Triples.
    :param hr: Home Runs.
    :param ab: At Bat.
    :return:
    '''
    return (h + 2 * _2b + 3 * _3b + 4 * hr) / ab


def ops(h, bb, hbp, ab, sf, _2b, _3b, hr):
    '''
    Calculate On-Base Plus Slugging (OPS) = OBP + SLG
    :param h: Hits.
    :param bb: Walks (Bases on Balls).
    :param hbp: Hit by Pitch.
    :param ab: At Bat.
    :param sf: Sacrifice Flies.
    :param _2b: Doubles.
    :param _3b: Triples.
    :param hr: Home Runs.
    :return:
    '''
    return obp(h, bb, hbp, ab, sf) + slg(h, _2b, _3b, hr, ab)


def babip(h, hr, _2b, _3b, ab, so):
    '''
    Calculate Batting Average on Balls In Play (BABIP) = (H - HR - 2B - 3B) / (AB - SO - HR + SF)
    :param h: Hits.
    :param hr: Home Runs.
    :param _2b: Doubles.
    :param _3b: Triples.
    :param ab: At Bat.
    :param so: Strike Outs.
    :return:
    '''
    return (h - hr - _2b - _3b) / (ab - so - hr + sf)
