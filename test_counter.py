def test_counter():
    from counter import Counter

    c = Counter()
    c['banana'] += 1

    assert c['banana'] == 1

    c['banana'] += 1
    assert c['banana'] == 2

    c['foo'] += 1
    assert c['foo'] == 1
