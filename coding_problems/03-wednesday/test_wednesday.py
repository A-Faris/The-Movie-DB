# pylint: skip-file

import pytest

from wednesday import meeting


def test_basic_test_1():
    assert meeting("Alexis:Wahl;John:Bell;Victoria:Schwarz;Abba:Dorny;Grace:Meta;Ann:Arno;Madison:STAN;Alex:Cornwell;Lewis:Kern;Megan:Stan;Alex:Korn") == "(ARNO, ANN)(BELL, JOHN)(CORNWELL, ALEX)(DORNY, ABBA)(KERN, LEWIS)(KORN, ALEX)(META, GRACE)(SCHWARZ, VICTORIA)(STAN, MADISON)(STAN, MEGAN)(WAHL, ALEXIS)"


def test_basic_test_2():
    assert meeting("John:Gates;Michael:Wahl;Megan:Bell;Paul:Dorries;James:Dorny;Lewis:Steve;Alex:Meta;Elizabeth:Russel;Anna:Korn;Ann:Kern;Amber:Cornwell") == "(BELL, MEGAN)(CORNWELL, AMBER)(DORNY, JAMES)(DORRIES, PAUL)(GATES, JOHN)(KERN, ANN)(KORN, ANNA)(META, ALEX)(RUSSEL, ELIZABETH)(STEVE, LEWIS)(WAHL, MICHAEL)"


def test_basic_test_3():
    assert meeting("Alex:Arno;Alissa:Cornwell;Sarah:Bell;Andrew:Dorries;Ann:Kern;Haley:Arno;Paul:Dorny;Madison:Kern") == "(ARNO, ALEX)(ARNO, HALEY)(BELL, SARAH)(CORNWELL, ALISSA)(DORNY, PAUL)(DORRIES, ANDREW)(KERN, ANN)(KERN, MADISON)"


def test_additional_test_1():
    assert meeting("Anna:Wahl;Grace:Gates;James:Russell;Elizabeth:Rudd;Victoria:STAN;Jacob:Wahl;Alex:Wahl;Antony:Gates;Alissa:Meta;Megan:Bell;Amandy:Stan;Anna:Steve") == "(BELL, MEGAN)(GATES, ANTONY)(GATES, GRACE)(META, ALISSA)(RUDD, ELIZABETH)(RUSSELL, JAMES)(STAN, AMANDY)(STAN, VICTORIA)(STEVE, ANNA)(WAHL, ALEX)(WAHL, ANNA)(WAHL, JACOB)"


def test_additional_test_2():
    assert meeting("Ann:Russel;John:Gates;Paul:Wahl;Alex:Tolkien;Ann:Bell;Lewis:Kern;Sarah:Rudd;Sydney:Korn;Madison:Meta") == "(BELL, ANN)(GATES, JOHN)(KERN, LEWIS)(KORN, SYDNEY)(META, MADISON)(RUDD, SARAH)(RUSSEL, ANN)(TOLKIEN, ALEX)(WAHL, PAUL)"


def test_additional_test_3():
    assert meeting("Paul:Arno;Matthew:Schwarz;Amandy:Meta;Grace:Meta;Ann:Arno;Alex:Schwarz;Jacob:Rudd;Amber:Cornwell") == "(ARNO, ANN)(ARNO, PAUL)(CORNWELL, AMBER)(META, AMANDY)(META, GRACE)(RUDD, JACOB)(SCHWARZ, ALEX)(SCHWARZ, MATTHEW)"


def test_additional_test_4():
    assert meeting("Abba:Bell;Lewis:Cornwell;Jacob:STAN;Matthew:Schwarz;Ann:STAN;Sophia:Gates;Victoria:Korn;Anna:Bell;Paul:Kern;Alissa:Tolkien") == "(BELL, ABBA)(BELL, ANNA)(CORNWELL, LEWIS)(GATES, SOPHIA)(KERN, PAUL)(KORN, VICTORIA)(SCHWARZ, MATTHEW)(STAN, ANN)(STAN, JACOB)(TOLKIEN, ALISSA)"


def test_additional_test_5():
    assert meeting("Victoria:Thorensen;Ann:Arno;Alexis:Wahl;Emily:Stan;Anna:STAN;Jacob:Korn;Sophia:Gates;Amber:Kern") == "(ARNO, ANN)(GATES, SOPHIA)(KERN, AMBER)(KORN, JACOB)(STAN, ANNA)(STAN, EMILY)(THORENSEN, VICTORIA)(WAHL, ALEXIS)"


def test_additional_test_6():
    assert meeting("Andrew:Arno;Jacob:Russell;Anna:STAN;Antony:Gates;Amber:Korn;Lewis:Dorries;Ann:Burroughs;Alex:Kern;Anna:Arno;Elizabeth:Kern;John:Schwarz;Sarah:STAN") == "(ARNO, ANDREW)(ARNO, ANNA)(BURROUGHS, ANN)(DORRIES, LEWIS)(GATES, ANTONY)(KERN, ALEX)(KERN, ELIZABETH)(KORN, AMBER)(RUSSELL, JACOB)(SCHWARZ, JOHN)(STAN, ANNA)(STAN, SARAH)"


def test_additional_test_7():
    assert meeting("Megan:Wahl;Alexis:Arno;Alex:Wahl;Grace:STAN;Amber:Kern;Amandy:Schwarz;Alissa:Stan;Paul:Kern;Ann:Meta;Lewis:Burroughs;Andrew:Bell") == "(ARNO, ALEXIS)(BELL, ANDREW)(BURROUGHS, LEWIS)(KERN, AMBER)(KERN, PAUL)(META, ANN)(SCHWARZ, AMANDY)(STAN, ALISSA)(STAN, GRACE)(WAHL, ALEX)(WAHL, MEGAN)"


@pytest.mark.parametrize("a,b",
                         [("Ann:Kern;Anna:Schwarz;Andrew:Russell;Abba:Rudd;Paul:Stan;Sophia:Meta;Ann:Tolkien;Alex:Bell;Alex:Cornwell;Alissa:Dorries;Robert:Wah", "(BELL, ALEX)(CORNWELL, ALEX)(DORRIES, ALISSA)(KERN, ANN)(META, SOPHIA)(RUDD, ABBA)(RUSSELL, ANDREW)(SCHWARZ, ANNA)(STAN, PAUL)(TOLKIEN, ANN)(WAH, ROBERT)"),
                          ("James:Dorries;Jacob:Arno;Sarah:Meta;Antony:Bell;Grace:Bell;Alex:Thorensen;Madison:Kern;Michael:Wah",
                           "(ARNO, JACOB)(BELL, ANTONY)(BELL, GRACE)(DORRIES, JAMES)(KERN, MADISON)(META, SARAH)(THORENSEN, ALEX)(WAH, MICHAEL)"),
                             ("Amber:Wahl;Elizabeth:STAN;Sarah:Bell;Emily:Kern;Robert:Thorensen;Sydney:Schwarz;Alex:Russel;Madison:Stev",
                              "(BELL, SARAH)(KERN, EMILY)(RUSSEL, ALEX)(SCHWARZ, SYDNEY)(STAN, ELIZABETH)(STEV, MADISON)(THORENSEN, ROBERT)(WAHL, AMBER)"),
                             ("Alex:Wahl;Megan:STAN;Alissa:Schwarz;Victoria:Arno;Alex:Korn;Ann:Rudd;Amber:Dorries;Lewis:Bell;Anna:Stan;Emily:Russell;Jacob:Met",
                              "(ARNO, VICTORIA)(BELL, LEWIS)(DORRIES, AMBER)(KORN, ALEX)(MET, JACOB)(RUDD, ANN)(RUSSELL, EMILY)(SCHWARZ, ALISSA)(STAN, ANNA)(STAN, MEGAN)(WAHL, ALEX)"),
                             ("Anna:Meta;Sophia:Bell;Alexis:Cornwell;Elizabeth:Kern;Madison:Korn;Ann:Russell;Alex:Stan;Sydney:Dorn",
                              "(BELL, SOPHIA)(CORNWELL, ALEXIS)(DORN, SYDNEY)(KERN, ELIZABETH)(KORN, MADISON)(META, ANNA)(RUSSELL, ANN)(STAN, ALEX)"),
                             ("Sophia:Bell;Paul:Arno;Alex:Meta;Victoria:Stan;Sarah:Korn;James:Kern;Alissa:Rudd;Andrew:Bell;Paul:Meta;Jacob:Gate",
                              "(ARNO, PAUL)(BELL, ANDREW)(BELL, SOPHIA)(GATE, JACOB)(KERN, JAMES)(KORN, SARAH)(META, ALEX)(META, PAUL)(RUDD, ALISSA)(STAN, VICTORIA)"),
                             ("Jacob:Meta;Ann:Russel;Antony:Meta;Lewis:Cornwell;Alex:Bell;Alex:Steve;Matthew:Bell;Andrew:Ker",
                              "(BELL, ALEX)(BELL, MATTHEW)(CORNWELL, LEWIS)(KER, ANDREW)(META, ANTONY)(META, JACOB)(RUSSEL, ANN)(STEVE, ALEX)"),
                             ("Lewis:Russell;Andrew:Wahl;Robert:Meta;Madison:STAN;Paul:Stan;Ann:Tolkien;Amandy:Rudd;Alex:Ker",
                              "(KER, ALEX)(META, ROBERT)(RUDD, AMANDY)(RUSSELL, LEWIS)(STAN, MADISON)(STAN, PAUL)(TOLKIEN, ANN)(WAHL, ANDREW)"),
                             ("Ann:Korn;Matthew:Gates;Madison:Kern;Robert:Steve;Elizabeth:Bell;Alex:STAN;Victoria:Wahl;Megan:Arno;Alex:Rud",
                              "(ARNO, MEGAN)(BELL, ELIZABETH)(GATES, MATTHEW)(KERN, MADISON)(KORN, ANN)(RUD, ALEX)(STAN, ALEX)(STEVE, ROBERT)(WAHL, VICTORIA)"),
                             ("Grace:STAN;John:Meta;Abba:Burroughs;Megan:Wahl;Sarah:Dorries;Sydney:Rudd;Ann:Bell;Amandy:Ker",
                              "(BELL, ANN)(BURROUGHS, ABBA)(DORRIES, SARAH)(KER, AMANDY)(META, JOHN)(RUDD, SYDNEY)(STAN, GRACE)(WAHL, MEGAN)"),
                             ("Lewis:Thorensen;Robert:Meta;Alexis:Gates;Andrew:Rudd;Anna:Schwarz;Ann:Korn;Alex:Schwarz;Amber:STAN;Megan:STA",
                              "(GATES, ALEXIS)(KORN, ANN)(META, ROBERT)(RUDD, ANDREW)(SCHWARZ, ALEX)(SCHWARZ, ANNA)(STA, MEGAN)(STAN, AMBER)(THORENSEN, LEWIS)"),
                             ("Ann:Bell;Alex:Burroughs;Lewis:Bell;Haley:Kern;Amandy:Meta;Grace:Wahl;Paul:Russell;Jacob:Schwarz;Emily:Wahl;Alex:Meta;Michael:Dorries;Sydney:Cornwel",
                              "(BELL, ANN)(BELL, LEWIS)(BURROUGHS, ALEX)(CORNWEL, SYDNEY)(DORRIES, MICHAEL)(KERN, HALEY)(META, ALEX)(META, AMANDY)(RUSSELL, PAUL)(SCHWARZ, JACOB)(WAHL, EMILY)(WAHL, GRACE)"),
                             ("James:Kern;Andrew:Meta;Ann:Thorensen;Sarah:Schwarz;Alex:Meta;Sophia:Tolkien;John:Dorny;Haley:Meta;Ann:STAN;Paul:Wahl;Emily:Schwar",
                              "(DORNY, JOHN)(KERN, JAMES)(META, ALEX)(META, ANDREW)(META, HALEY)(SCHWAR, EMILY)(SCHWARZ, SARAH)(STAN, ANN)(THORENSEN, ANN)(TOLKIEN, SOPHIA)(WAHL, PAUL)"),
                             ("Megan:Cornwell;Emily:Rudd;Elizabeth:Kern;Michael:Meta;Alex:Meta;Amandy:Dorny;Alex:Steve;Andrew:Burroughs;Jacob:Meta;John:Sta",
                              "(BURROUGHS, ANDREW)(CORNWELL, MEGAN)(DORNY, AMANDY)(KERN, ELIZABETH)(META, ALEX)(META, JACOB)(META, MICHAEL)(RUDD, EMILY)(STA, JOHN)(STEVE, ALEX)"),
                             ("Megan:Wahl;Alissa:Arno;James:Gates;Sydney:Dorries;Madison:Cornwell;Emily:Thorensen;Jacob:Meta;Antony:Cornwel",
                              "(ARNO, ALISSA)(CORNWEL, ANTONY)(CORNWELL, MADISON)(DORRIES, SYDNEY)(GATES, JAMES)(META, JACOB)(THORENSEN, EMILY)(WAHL, MEGAN)"),
                             ("Matthew:Rudd;Alex:Dorny;Amber:Wahl;Megan:Dorries;Amandy:Russell;Victoria:Cornwell;John:Meta;Paul:Ker",
                              "(CORNWELL, VICTORIA)(DORNY, ALEX)(DORRIES, MEGAN)(KER, PAUL)(META, JOHN)(RUDD, MATTHEW)(RUSSELL, AMANDY)(WAHL, AMBER)"),
                             ("Anna:Bell;Alexis:Meta;Sydney:Meta;Haley:Russel;Ann:Schwarz;Amber:Tolkien;Antony:Cornwell;Alex:Meta;Ann:Kern;Elizabeth:STAN;Lewis:Wah",
                              "(BELL, ANNA)(CORNWELL, ANTONY)(KERN, ANN)(META, ALEX)(META, ALEXIS)(META, SYDNEY)(RUSSEL, HALEY)(SCHWARZ, ANN)(STAN, ELIZABETH)(TOLKIEN, AMBER)(WAH, LEWIS)"),
                             ("Robert:Korn;Ann:Dorries;Sydney:Bell;Paul:Meta;Matthew:Gates;Victoria:Kern;Amber:Dorny;Haley:STA",
                              "(BELL, SYDNEY)(DORNY, AMBER)(DORRIES, ANN)(GATES, MATTHEW)(KERN, VICTORIA)(KORN, ROBERT)(META, PAUL)(STA, HALEY)"),
                             ("Sydney:Meta;Robert:Cornwell;Alexis:Dorries;Paul:Steve;Sarah:Stan;Amandy:Gates;Haley:Meta;Lewis:Thorensen;Alex:Kern;Madison:Dorny;James:Schwarz;Ann:Arn",
                              "(ARN, ANN)(CORNWELL, ROBERT)(DORNY, MADISON)(DORRIES, ALEXIS)(GATES, AMANDY)(KERN, ALEX)(META, HALEY)(META, SYDNEY)(SCHWARZ, JAMES)(STAN, SARAH)(STEVE, PAUL)(THORENSEN, LEWIS)"),
                             ("Anna:Thorensen;Grace:Korn;Emily:Korn;Paul:Steve;Paul:Dorny;James:Schwarz;Madison:Wahl;Sarah:Arno;Antony:Burrough",
                              "(ARNO, SARAH)(BURROUGH, ANTONY)(DORNY, PAUL)(KORN, EMILY)(KORN, GRACE)(SCHWARZ, JAMES)(STEVE, PAUL)(THORENSEN, ANNA)(WAHL, MADISON)"),
                             ("Sarah:Wahl;Grace:Bell;Sydney:Korn;Alissa:Dorries;Victoria:Stan;Alex:Kern;James:Wahl;Amber:Kor",
                              "(BELL, GRACE)(DORRIES, ALISSA)(KERN, ALEX)(KOR, AMBER)(KORN, SYDNEY)(STAN, VICTORIA)(WAHL, JAMES)(WAHL, SARAH)"),
                             ("Alex:Russell;Sydney:Bell;John:STAN;Megan:Steve;Victoria:Rudd;Jacob:Burroughs;James:Wahl;Ann:Ker",
                              "(BELL, SYDNEY)(BURROUGHS, JACOB)(KER, ANN)(RUDD, VICTORIA)(RUSSELL, ALEX)(STAN, JOHN)(STEVE, MEGAN)(WAHL, JAMES)"),
                             ("Matthew:Stan;Amber:Wahl;Ann:Korn;Haley:Gates;John:Bell;Alissa:STAN;Abba:Arno;Alexis:Tolkien;Sarah:Meta;Alex:Schwarz;Ann:Russel;Alex:Kor",
                              "(ARNO, ABBA)(BELL, JOHN)(GATES, HALEY)(KOR, ALEX)(KORN, ANN)(META, SARAH)(RUSSEL, ANN)(SCHWARZ, ALEX)(STAN, ALISSA)(STAN, MATTHEW)(TOLKIEN, ALEXIS)(WAHL, AMBER)"),
                             ("Matthew:Schwarz;Haley:Korn;Megan:Wahl;Lewis:Gates;Ann:Stan;Ann:Wahl;Robert:Thorensen;Grace:Wahl;Anna:Meta;Sophia:Meta;Michael:Schwar",
                              "(GATES, LEWIS)(KORN, HALEY)(META, ANNA)(META, SOPHIA)(SCHWAR, MICHAEL)(SCHWARZ, MATTHEW)(STAN, ANN)(THORENSEN, ROBERT)(WAHL, ANN)(WAHL, GRACE)(WAHL, MEGAN)"),
                             ("Haley:Schwarz;James:Russell;Ann:Stan;Grace:Dorries;Victoria:Thorensen;Paul:Burroughs;Sydney:Gates;Emily:Meta;Paul:Bell;Anna:Arn",
                              "(ARN, ANNA)(BELL, PAUL)(BURROUGHS, PAUL)(DORRIES, GRACE)(GATES, SYDNEY)(META, EMILY)(RUSSELL, JAMES)(SCHWARZ, HALEY)(STAN, ANN)(THORENSEN, VICTORIA)"),
                             ("Alissa:Burroughs;Antony:Gates;Alex:Kern;Anna:Gates;Jacob:Meta;Sarah:Arno;Andrew:Bell;Michael:Bel",
                              "(ARNO, SARAH)(BEL, MICHAEL)(BELL, ANDREW)(BURROUGHS, ALISSA)(GATES, ANNA)(GATES, ANTONY)(KERN, ALEX)(META, JACOB)"),
                             ("Emily:Bell;John:Dorries;Amber:Arno;Ann:Wahl;Madison:Korn;James:Kern;Alex:Russel;Elizabeth:Met",
                              "(ARNO, AMBER)(BELL, EMILY)(DORRIES, JOHN)(KERN, JAMES)(KORN, MADISON)(MET, ELIZABETH)(RUSSEL, ALEX)(WAHL, ANN)"),
                             ("Jacob:Wahl;Amandy:Meta;Alexis:Russel;Alex:Cornwell;Alex:Korn;Robert:Meta;Abba:Wahl;Alex:Wahl;Paul:Cornwell;Antony:Bell;Sophia:Tolkie",
                              "(BELL, ANTONY)(CORNWELL, ALEX)(CORNWELL, PAUL)(KORN, ALEX)(META, AMANDY)(META, ROBERT)(RUSSEL, ALEXIS)(TOLKIE, SOPHIA)(WAHL, ABBA)(WAHL, ALEX)(WAHL, JACOB)"),
                             ("Sarah:Meta;Ann:Gates;Alexis:Kern;Paul:Meta;Anna:Wahl;Ann:Schwarz;Amber:Thorensen;Ann:Russel",
                              "(GATES, ANN)(KERN, ALEXIS)(META, PAUL)(META, SARAH)(RUSSEL, ANN)(SCHWARZ, ANN)(THORENSEN, AMBER)(WAHL, ANNA)"),
                             ("Megan:Wahl;John:Schwarz;Antony:Bell;Andrew:Stan;Lewis:Steve;Alex:Gates;Elizabeth:Bell;Robert:Tolkien;Ann:Kern;Alex:Rud",
                              "(BELL, ANTONY)(BELL, ELIZABETH)(GATES, ALEX)(KERN, ANN)(RUD, ALEX)(SCHWARZ, JOHN)(STAN, ANDREW)(STEVE, LEWIS)(TOLKIEN, ROBERT)(WAHL, MEGAN)"),
                             ("Michael:Korn;Anna:STAN;Anna:Bell;Sophia:Schwarz;Paul:Gates;Haley:STAN;Ann:Tolkien;Antony:Kern;Ann:Rud",
                              "(BELL, ANNA)(GATES, PAUL)(KERN, ANTONY)(KORN, MICHAEL)(RUD, ANN)(SCHWARZ, SOPHIA)(STAN, ANNA)(STAN, HALEY)(TOLKIEN, ANN)"),
                             ("Sophia:STAN;Michael:Arno;Ann:Wahl;Ann:Bell;Paul:Tolkien;Jacob:Wahl;Alex:Bell;Amandy:Dorries;Alex:STAN;Alexis:Wahl;Matthew:Met",
                              "(ARNO, MICHAEL)(BELL, ALEX)(BELL, ANN)(DORRIES, AMANDY)(MET, MATTHEW)(STAN, ALEX)(STAN, SOPHIA)(TOLKIEN, PAUL)(WAHL, ALEXIS)(WAHL, ANN)(WAHL, JACOB)"),
                             ("Antony:Russel;Matthew:STAN;Alex:Kern;Alexis:Wahl;Jacob:Korn;James:Gates;Paul:Tolkien;Robert:Dorries;Anna:Bel",
                              "(BEL, ANNA)(DORRIES, ROBERT)(GATES, JAMES)(KERN, ALEX)(KORN, JACOB)(RUSSEL, ANTONY)(STAN, MATTHEW)(TOLKIEN, PAUL)(WAHL, ALEXIS)"),
                             ("Alissa:Meta;Madison:Cornwell;James:Kern;Matthew:Bell;Anna:Thorensen;Amandy:Russell;Alex:Russel;Victoria:Korn;Ann:Kern;Michael:Schwar",
                              "(BELL, MATTHEW)(CORNWELL, MADISON)(KERN, ANN)(KERN, JAMES)(KORN, VICTORIA)(META, ALISSA)(RUSSEL, ALEX)(RUSSELL, AMANDY)(SCHWAR, MICHAEL)(THORENSEN, ANNA)"),
                             ("Emily:Bell;Amber:Meta;Ann:Wahl;Elizabeth:Bell;Amandy:Stan;Jacob:Gates;Antony:Kern;Alexis:Russel",
                              "(BELL, ELIZABETH)(BELL, EMILY)(GATES, JACOB)(KERN, ANTONY)(META, AMBER)(RUSSEL, ALEXIS)(STAN, AMANDY)(WAHL, ANN)"),
                             ("Jacob:Dorries;Haley:Korn;Alex:Tolkien;Alex:Stan;Ann:Wahl;Alex:Bell;Grace:Wahl;Anna:Bell;Abba:Wahl;Lewis:Schwar",
                              "(BELL, ALEX)(BELL, ANNA)(DORRIES, JACOB)(KORN, HALEY)(SCHWAR, LEWIS)(STAN, ALEX)(TOLKIEN, ALEX)(WAHL, ABBA)(WAHL, ANN)(WAHL, GRACE)"),
                             ("Victoria:Korn;Sophia:Russell;Antony:Thorensen;Andrew:Burroughs;Grace:Gates;Sydney:Arno;Madison:Arno;Anna:Rudd;Alex:Tolkien;Haley:Dorrie",
                              "(ARNO, MADISON)(ARNO, SYDNEY)(BURROUGHS, ANDREW)(DORRIE, HALEY)(GATES, GRACE)(KORN, VICTORIA)(RUDD, ANNA)(RUSSELL, SOPHIA)(THORENSEN, ANTONY)(TOLKIEN, ALEX)"),
                             ("Elizabeth:Kern;Sophia:Schwarz;James:STAN;Megan:Dorny;Alex:Gates;John:STAN;Ann:Dorries;Anna:Bell;Matthew:Stan;Andrew:Burroughs;Amber:Wah",
                              "(BELL, ANNA)(BURROUGHS, ANDREW)(DORNY, MEGAN)(DORRIES, ANN)(GATES, ALEX)(KERN, ELIZABETH)(SCHWARZ, SOPHIA)(STAN, JAMES)(STAN, JOHN)(STAN, MATTHEW)(WAH, AMBER)"),
                             ("Sarah:Korn;Megan:Steve;Alex:Cornwell;Haley:Dorny;Abba:Meta;John:Thorensen;Alexis:STAN;Grace:Ker",
                              "(CORNWELL, ALEX)(DORNY, HALEY)(KER, GRACE)(KORN, SARAH)(META, ABBA)(STAN, ALEXIS)(STEVE, MEGAN)(THORENSEN, JOHN)"),
                             ("Paul:Stan;Anna:Bell;Grace:Meta;Antony:Meta;Megan:Korn;Abba:Schwarz;Paul:Dorries;Emily:Arno;Alex:Bell;Amandy:Korn;Sarah:Steve;James:Wah",
                              "(ARNO, EMILY)(BELL, ALEX)(BELL, ANNA)(DORRIES, PAUL)(KORN, AMANDY)(KORN, MEGAN)(META, ANTONY)(META, GRACE)(SCHWARZ, ABBA)(STAN, PAUL)(STEVE, SARAH)(WAH, JAMES)"),
                             ("Sarah:Rudd;Paul:Dorny;Alex:Bell;John:Kern;Anna:Meta;Abba:Thorensen;Amandy:Korn;Sydney:Meta;Matthew:Korn;Lewis:Wahl;James:Gate",
                              "(BELL, ALEX)(DORNY, PAUL)(GATE, JAMES)(KERN, JOHN)(KORN, AMANDY)(KORN, MATTHEW)(META, ANNA)(META, SYDNEY)(RUDD, SARAH)(THORENSEN, ABBA)(WAHL, LEWIS)"),
                             ("Abba:Tolkien;Andrew:Thorensen;Sydney:Wahl;Ann:Stan;Lewis:Russel;Ann:STAN;Amber:Meta;Michael:Arno;Anna:Wahl;Sophia:Schwar",
                              "(ARNO, MICHAEL)(META, AMBER)(RUSSEL, LEWIS)(SCHWAR, SOPHIA)(STAN, ANN)(STAN, ANN)(THORENSEN, ANDREW)(TOLKIEN, ABBA)(WAHL, ANNA)(WAHL, SYDNEY)"),
                             ("Amandy:Cornwell;Alexis:Meta;Anna:STAN;Grace:Steve;Robert:Tolkien;Alex:Bell;Megan:Kern;Sydney:Wah",
                              "(BELL, ALEX)(CORNWELL, AMANDY)(KERN, MEGAN)(META, ALEXIS)(STAN, ANNA)(STEVE, GRACE)(TOLKIEN, ROBERT)(WAH, SYDNEY)"),
                             ("Victoria:Bell;Paul:STAN;Jacob:Bell;Andrew:Gates;Anna:Cornwell;Ann:Korn;Anna:Korn;Robert:Arno;Matthew:Kern;Elizabeth:Gates;John:Meta;Megan:Dorrie",
                              "(ARNO, ROBERT)(BELL, JACOB)(BELL, VICTORIA)(CORNWELL, ANNA)(DORRIE, MEGAN)(GATES, ANDREW)(GATES, ELIZABETH)(KERN, MATTHEW)(KORN, ANN)(KORN, ANNA)(META, JOHN)(STAN, PAUL)"),
                             ("Victoria:Arno;Sophia:Tolkien;Elizabeth:Russel;Matthew:Cornwell;Emily:Wahl;James:Korn;Andrew:Arno;Jacob:STA",
                              "(ARNO, ANDREW)(ARNO, VICTORIA)(CORNWELL, MATTHEW)(KORN, JAMES)(RUSSEL, ELIZABETH)(STA, JACOB)(TOLKIEN, SOPHIA)(WAHL, EMILY)"),
                             ("Lewis:Wahl;Grace:Schwarz;Madison:Thorensen;Sydney:Wahl;Emily:Steve;Amber:Bell;Sophia:Korn;Ann:Stan;Jacob:Schwarz;Abba:Gates;Andrew:Gates;John:Met",
                              "(BELL, AMBER)(GATES, ABBA)(GATES, ANDREW)(KORN, SOPHIA)(MET, JOHN)(SCHWARZ, GRACE)(SCHWARZ, JACOB)(STAN, ANN)(STEVE, EMILY)(THORENSEN, MADISON)(WAHL, LEWIS)(WAHL, SYDNEY)"),
                             ("Victoria:Schwarz;Paul:Kern;Sophia:Russell;Antony:Bell;Ann:Arno;Grace:Thorensen;Amandy:Dorny;Amber:STA",
                              "(ARNO, ANN)(BELL, ANTONY)(DORNY, AMANDY)(KERN, PAUL)(RUSSELL, SOPHIA)(SCHWARZ, VICTORIA)(STA, AMBER)(THORENSEN, GRACE)"),
                             ("Jacob:Kern;Megan:Rudd;Paul:Wahl;Matthew:Meta;Paul:Meta;Ann:Gates;Anna:Arno;Michael:Wah",
                              "(ARNO, ANNA)(GATES, ANN)(KERN, JACOB)(META, MATTHEW)(META, PAUL)(RUDD, MEGAN)(WAH, MICHAEL)(WAHL, PAUL)"),
                             ("Ann:Kern;Andrew:Stan;Robert:Schwarz;Ann:Bell;Haley:STAN;Alex:Arno;Ann:Cornwell;Alexis:Russel;Sydney:Korn;James:Dorrie",
                              "(ARNO, ALEX)(BELL, ANN)(CORNWELL, ANN)(DORRIE, JAMES)(KERN, ANN)(KORN, SYDNEY)(RUSSEL, ALEXIS)(SCHWARZ, ROBERT)(STAN, ANDREW)(STAN, HALEY)"),
                             ("Sydney:Bell;Emily:Rudd;Elizabeth:Russell;Ann:Burroughs;Haley:Cornwell;Matthew:Russel;Grace:Meta;Anna:Kern;Sophia:Thorensen;Ann:Schwar",
                              "(BELL, SYDNEY)(BURROUGHS, ANN)(CORNWELL, HALEY)(KERN, ANNA)(META, GRACE)(RUDD, EMILY)(RUSSEL, MATTHEW)(RUSSELL, ELIZABETH)(SCHWAR, ANN)(THORENSEN, SOPHIA)"),
                             ("Matthew:Cornwell;Jacob:Arno;Victoria:Russel;Amber:Burroughs;Sarah:Arno;Haley:Kern;Emily:Dorny;Paul:Wahl;Sydney:Wahl;Megan:Dorrie",
                              "(ARNO, JACOB)(ARNO, SARAH)(BURROUGHS, AMBER)(CORNWELL, MATTHEW)(DORNY, EMILY)(DORRIE, MEGAN)(KERN, HALEY)(RUSSEL, VICTORIA)(WAHL, PAUL)(WAHL, SYDNEY)"),
                             ("Robert:STAN;Anna:Wahl;Amandy:Gates;Ann:Schwarz;Elizabeth:Stan;Grace:Wahl;Sarah:Cornwell;Lewis:Russel",
                              "(CORNWELL, SARAH)(GATES, AMANDY)(RUSSEL, LEWIS)(SCHWARZ, ANN)(STAN, ELIZABETH)(STAN, ROBERT)(WAHL, ANNA)(WAHL, GRACE)"),
                             ("Alexis:Korn;Anna:Wahl;Emily:Steve;Ann:Wahl;Megan:Cornwell;Sarah:Schwarz;Ann:Russell;Alissa:Ker",
                              "(CORNWELL, MEGAN)(KER, ALISSA)(KORN, ALEXIS)(RUSSELL, ANN)(SCHWARZ, SARAH)(STEVE, EMILY)(WAHL, ANN)(WAHL, ANNA)"),
                             ("Paul:Rudd;Alex:Stan;Haley:Gates;Grace:Schwarz;Elizabeth:Wahl;Ann:Wahl;Michael:Cornwell;Victoria:Korn;Abba:Met",
                              "(CORNWELL, MICHAEL)(GATES, HALEY)(KORN, VICTORIA)(MET, ABBA)(RUDD, PAUL)(SCHWARZ, GRACE)(STAN, ALEX)(WAHL, ANN)(WAHL, ELIZABETH)"),
                             ("Michael:Burroughs;Megan:Bell;John:Russell;Ann:Meta;Amber:Bell;Grace:Thorensen;Matthew:Gates;Elizabeth:Ker",
                              "(BELL, AMBER)(BELL, MEGAN)(BURROUGHS, MICHAEL)(GATES, MATTHEW)(KER, ELIZABETH)(META, ANN)(RUSSELL, JOHN)(THORENSEN, GRACE)"),
                             ("Madison:STAN;Alex:Wahl;Andrew:Tolkien;Alexis:Kern;Sarah:Korn;Elizabeth:Arno;James:Steve;Anna:Rudd;Megan:Russel;Paul:Meta;Amber:Burrough",
                              "(ARNO, ELIZABETH)(BURROUGH, AMBER)(KERN, ALEXIS)(KORN, SARAH)(META, PAUL)(RUDD, ANNA)(RUSSEL, MEGAN)(STAN, MADISON)(STEVE, JAMES)(TOLKIEN, ANDREW)(WAHL, ALEX)"),
                             ("Haley:Kern;Alissa:Meta;Jacob:Cornwell;Antony:Russell;Sarah:STAN;Abba:Dorries;Sophia:Arno;Amandy:Kern;Matthew:Tolkien;Lewis:Gate",
                              "(ARNO, SOPHIA)(CORNWELL, JACOB)(DORRIES, ABBA)(GATE, LEWIS)(KERN, AMANDY)(KERN, HALEY)(META, ALISSA)(RUSSELL, ANTONY)(STAN, SARAH)(TOLKIEN, MATTHEW)"),
                             ("John:Gates;Madison:Meta;Paul:Cornwell;Alexis:Tolkien;Haley:Kern;Sophia:Bell;Michael:Wahl;Jacob:Russell;Megan:Bel",
                              "(BEL, MEGAN)(BELL, SOPHIA)(CORNWELL, PAUL)(GATES, JOHN)(KERN, HALEY)(META, MADISON)(RUSSELL, JACOB)(TOLKIEN, ALEXIS)(WAHL, MICHAEL)"),
                             ("Ann:Russel;Paul:Gates;Alexis:Wahl;Jacob:Cornwell;Megan:Rudd;Anna:Schwarz;Alissa:Korn;Alex:Meta;Grace:Burroughs;Alex:Bel",
                              "(BEL, ALEX)(BURROUGHS, GRACE)(CORNWELL, JACOB)(GATES, PAUL)(KORN, ALISSA)(META, ALEX)(RUDD, MEGAN)(RUSSEL, ANN)(SCHWARZ, ANNA)(WAHL, ALEXIS)"),
                             ("Amandy:Gates;Abba:Wahl;Victoria:Rudd;Ann:Dorny;Lewis:Schwarz;Anna:Wahl;Andrew:STAN;Grace:Arno;Sydney:Bell;Paul:Bel",
                              "(ARNO, GRACE)(BEL, PAUL)(BELL, SYDNEY)(DORNY, ANN)(GATES, AMANDY)(RUDD, VICTORIA)(SCHWARZ, LEWIS)(STAN, ANDREW)(WAHL, ABBA)(WAHL, ANNA)"),
                             ("Andrew:STAN;Sophia:Dorries;Amandy:Dorny;James:Russell;Jacob:Kern;Sydney:STAN;Lewis:Thorensen;Haley:Wah",
                              "(DORNY, AMANDY)(DORRIES, SOPHIA)(KERN, JACOB)(RUSSELL, JAMES)(STAN, ANDREW)(STAN, SYDNEY)(THORENSEN, LEWIS)(WAH, HALEY)"),
                             ("Robert:STAN;Victoria:Rudd;Emily:Schwarz;Alissa:Kern;Ann:Meta;Amandy:Burroughs;Elizabeth:Thorensen;Sophia:Dorny;Abba:Stan;Sarah:Ker",
                              "(BURROUGHS, AMANDY)(DORNY, SOPHIA)(KER, SARAH)(KERN, ALISSA)(META, ANN)(RUDD, VICTORIA)(SCHWARZ, EMILY)(STAN, ABBA)(STAN, ROBERT)(THORENSEN, ELIZABETH)"),
                             ("Jacob:Schwarz;Alex:Dorny;Madison:Wahl;Anna:Russel;Andrew:Korn;Abba:Gates;Sophia:Stan;Lewis:Wah",
                              "(DORNY, ALEX)(GATES, ABBA)(KORN, ANDREW)(RUSSEL, ANNA)(SCHWARZ, JACOB)(STAN, SOPHIA)(WAH, LEWIS)(WAHL, MADISON)"),
                             ("Sophia:Kern;Antony:Wahl;Alex:Schwarz;Michael:Cornwell;Jacob:Thorensen;John:Wahl;Robert:Rudd;Alissa:Arno;Andrew:Schwar",
                              "(ARNO, ALISSA)(CORNWELL, MICHAEL)(KERN, SOPHIA)(RUDD, ROBERT)(SCHWAR, ANDREW)(SCHWARZ, ALEX)(THORENSEN, JACOB)(WAHL, ANTONY)(WAHL, JOHN)"),
                             ("Alex:Russell;Andrew:Korn;Ann:Meta;Abba:Wahl;Ann:Meta;Madison:Cornwell;Antony:Tolkien;Elizabeth:Dorny;Haley:Korn;Alex:Gate",
                              "(CORNWELL, MADISON)(DORNY, ELIZABETH)(GATE, ALEX)(KORN, ANDREW)(KORN, HALEY)(META, ANN)(META, ANN)(RUSSELL, ALEX)(TOLKIEN, ANTONY)(WAHL, ABBA)"),
                             ("Anna:Bell;Grace:Kern;Amandy:Kern;Haley:Meta;Alexis:Thorensen;Alex:Cornwell;Ann:Arno;Antony:Wahl;Paul:STAN;Alex:Schwarz;Anna:Meta;Lewis:Russel",
                              "(ARNO, ANN)(BELL, ANNA)(CORNWELL, ALEX)(KERN, AMANDY)(KERN, GRACE)(META, ANNA)(META, HALEY)(RUSSEL, LEWIS)(SCHWARZ, ALEX)(STAN, PAUL)(THORENSEN, ALEXIS)(WAHL, ANTONY)"),
                             ("Robert:Wahl;Emily:Kern;Ann:Korn;Michael:Kern;Anna:Arno;Amber:Russell;Alex:Bell;Megan:Rudd;Lewis:Tolkie",
                              "(ARNO, ANNA)(BELL, ALEX)(KERN, EMILY)(KERN, MICHAEL)(KORN, ANN)(RUDD, MEGAN)(RUSSELL, AMBER)(TOLKIE, LEWIS)(WAHL, ROBERT)"),
                             ("Amber:Meta;Alexis:Korn;Grace:Schwarz;Amandy:Wahl;Robert:Kern;Abba:Burroughs;Lewis:Schwarz;Emily:Arn",
                              "(ARN, EMILY)(BURROUGHS, ABBA)(KERN, ROBERT)(KORN, ALEXIS)(META, AMBER)(SCHWARZ, GRACE)(SCHWARZ, LEWIS)(WAHL, AMANDY)"),
                             ("Ann:Tolkien;Lewis:Russel;Antony:Kern;Paul:STAN;Anna:Burroughs;Matthew:Cornwell;Ann:Bell;Emily:Met",
                              "(BELL, ANN)(BURROUGHS, ANNA)(CORNWELL, MATTHEW)(KERN, ANTONY)(MET, EMILY)(RUSSEL, LEWIS)(STAN, PAUL)(TOLKIEN, ANN)"),
                             ("Alex:Wahl;Haley:Wahl;Alex:Russel;Andrew:Stan;Anna:Korn;Robert:Kern;Madison:Bell;Emily:Cornwel",
                              "(BELL, MADISON)(CORNWEL, EMILY)(KERN, ROBERT)(KORN, ANNA)(RUSSEL, ALEX)(STAN, ANDREW)(WAHL, ALEX)(WAHL, HALEY)"),
                             ("Jacob:Bell;James:Cornwell;Elizabeth:Gates;Alex:Kern;Lewis:STAN;John:Arno;Ann:Wahl;Andrew:Schwar",
                              "(ARNO, JOHN)(BELL, JACOB)(CORNWELL, JAMES)(GATES, ELIZABETH)(KERN, ALEX)(SCHWAR, ANDREW)(STAN, LEWIS)(WAHL, ANN)"),
                             ("Megan:Wahl;Robert:Bell;Amandy:Dorries;Grace:Cornwell;Madison:Wahl;Alissa:Russell;Paul:Meta;Alex:Rudd;Amber:Meta;Andrew:Wahl;Anna:Russel;Michael:Thorense",
                              "(BELL, ROBERT)(CORNWELL, GRACE)(DORRIES, AMANDY)(META, AMBER)(META, PAUL)(RUDD, ALEX)(RUSSEL, ANNA)(RUSSELL, ALISSA)(THORENSE, MICHAEL)(WAHL, ANDREW)(WAHL, MADISON)(WAHL, MEGAN)"),
                             ("Madison:Thorensen;Megan:Cornwell;Haley:Arno;Matthew:Dorries;Sophia:Burroughs;James:Gates;Amber:Meta;John:Arn",
                              "(ARN, JOHN)(ARNO, HALEY)(BURROUGHS, SOPHIA)(CORNWELL, MEGAN)(DORRIES, MATTHEW)(GATES, JAMES)(META, AMBER)(THORENSEN, MADISON)"),
                             ("James:Wahl;Andrew:Wahl;Robert:Stan;Antony:Meta;Anna:Steve;Anna:Wahl;Alexis:Cornwell;Amber:Bell;Haley:Bel",
                              "(BEL, HALEY)(BELL, AMBER)(CORNWELL, ALEXIS)(META, ANTONY)(STAN, ROBERT)(STEVE, ANNA)(WAHL, ANDREW)(WAHL, ANNA)(WAHL, JAMES)"),
                             ("Matthew:Burroughs;Sydney:Stan;Alex:Wahl;James:Gates;Antony:Meta;Jacob:Russell;Andrew:Steve;Ann:Korn;Ann:Cornwell;Lewis:STA",
                              "(BURROUGHS, MATTHEW)(CORNWELL, ANN)(GATES, JAMES)(KORN, ANN)(META, ANTONY)(RUSSELL, JACOB)(STA, LEWIS)(STAN, SYDNEY)(STEVE, ANDREW)(WAHL, ALEX)"),
                             ("Ann:Kern;Alex:Arno;Grace:Cornwell;John:Dorny;Matthew:Gates;Michael:Arno;Alex:Wahl;Anna:Kor",
                              "(ARNO, ALEX)(ARNO, MICHAEL)(CORNWELL, GRACE)(DORNY, JOHN)(GATES, MATTHEW)(KERN, ANN)(KOR, ANNA)(WAHL, ALEX)"),
                             ("Sophia:Wahl;Amber:Bell;Elizabeth:Russel;Madison:Tolkien;Ann:Thorensen;Paul:Meta;James:Cornwell;Matthew:Arno;Ann:Ker",
                              "(ARNO, MATTHEW)(BELL, AMBER)(CORNWELL, JAMES)(KER, ANN)(META, PAUL)(RUSSEL, ELIZABETH)(THORENSEN, ANN)(TOLKIEN, MADISON)(WAHL, SOPHIA)"),
                             ("Megan:Meta;Paul:Burroughs;Alissa:Wahl;Ann:Bell;Sydney:Schwarz;Lewis:STAN;Sarah:Korn;Michael:Ker",
                              "(BELL, ANN)(BURROUGHS, PAUL)(KER, MICHAEL)(KORN, SARAH)(META, MEGAN)(SCHWARZ, SYDNEY)(STAN, LEWIS)(WAHL, ALISSA)"),
                             ("Emily:Rudd;Madison:Wahl;Paul:STAN;Lewis:Bell;Sarah:Kern;Haley:Dorny;Megan:Meta;Amber:Arno;Andrew:Bell;Sophia:Kern;Victoria:Meta;Sydney:Dorrie",
                              "(ARNO, AMBER)(BELL, ANDREW)(BELL, LEWIS)(DORNY, HALEY)(DORRIE, SYDNEY)(KERN, SARAH)(KERN, SOPHIA)(META, MEGAN)(META, VICTORIA)(RUDD, EMILY)(STAN, PAUL)(WAHL, MADISON)"),
                             ("Madison:Cornwell;Amandy:Kern;Antony:Arno;Alex:Schwarz;Elizabeth:Meta;Alexis:Meta;Victoria:Bell;Anna:Rud",
                              "(ARNO, ANTONY)(BELL, VICTORIA)(CORNWELL, MADISON)(KERN, AMANDY)(META, ALEXIS)(META, ELIZABETH)(RUD, ANNA)(SCHWARZ, ALEX)"),
                             ("Anna:Cornwell;Victoria:Wahl;Sophia:Kern;John:Kern;Alex:Bell;Paul:Russel;Alex:Korn;Emily:Gates;Megan:Schwar",
                              "(BELL, ALEX)(CORNWELL, ANNA)(GATES, EMILY)(KERN, JOHN)(KERN, SOPHIA)(KORN, ALEX)(RUSSEL, PAUL)(SCHWAR, MEGAN)(WAHL, VICTORIA)"),
                             ("Ann:Wahl;Elizabeth:Meta;Madison:Cornwell;Andrew:Schwarz;Antony:Cornwell;Michael:Wahl;Emily:Russell;Paul:Gates;Alex:Bell;Alexis:Ker",
                              "(BELL, ALEX)(CORNWELL, ANTONY)(CORNWELL, MADISON)(GATES, PAUL)(KER, ALEXIS)(META, ELIZABETH)(RUSSELL, EMILY)(SCHWARZ, ANDREW)(WAHL, ANN)(WAHL, MICHAEL)"),
                             ("Lewis:Kern;Ann:Gates;Anna:STAN;Paul:Russel;Anna:Bell;Alexis:Kern;Elizabeth:Thorensen;Amandy:Meta;Andrew:Tolkien;Alissa:Gates;Megan:Wahl;James:Wah",
                              "(BELL, ANNA)(GATES, ALISSA)(GATES, ANN)(KERN, ALEXIS)(KERN, LEWIS)(META, AMANDY)(RUSSEL, PAUL)(STAN, ANNA)(THORENSEN, ELIZABETH)(TOLKIEN, ANDREW)(WAH, JAMES)(WAHL, MEGAN)"),
                             ("Amber:Bell;Ann:Kern;Paul:Meta;Grace:Schwarz;Sydney:Thorensen;Ann:Stan;Ann:Bell;Megan:Wahl;Emily:Cornwell;Lewis:Arno;Jacob:Wahl;Alex:Met",
                              "(ARNO, LEWIS)(BELL, AMBER)(BELL, ANN)(CORNWELL, EMILY)(KERN, ANN)(MET, ALEX)(META, PAUL)(SCHWARZ, GRACE)(STAN, ANN)(THORENSEN, SYDNEY)(WAHL, JACOB)(WAHL, MEGAN)"),
                             ("Alexis:STAN;Sarah:Arno;Robert:Burroughs;Elizabeth:Cornwell;Jacob:Meta;Megan:STAN;Alex:Kern;Ann:Kern;Amandy:Dorny;Haley:Korn;Alex:Bell;Alissa:Kor",
                              "(ARNO, SARAH)(BELL, ALEX)(BURROUGHS, ROBERT)(CORNWELL, ELIZABETH)(DORNY, AMANDY)(KERN, ALEX)(KERN, ANN)(KOR, ALISSA)(KORN, HALEY)(META, JACOB)(STAN, ALEXIS)(STAN, MEGAN)"),
                             ("Ann:Thorensen;Paul:Gates;Amandy:Tolkien;James:Korn;Anna:Rudd;Sarah:STAN;Alex:STAN;Amber:Cornwell;Alex:Arno;Sydney:Schwarz;Ann:Wahl;Anna:Dorn",
                              "(ARNO, ALEX)(CORNWELL, AMBER)(DORN, ANNA)(GATES, PAUL)(KORN, JAMES)(RUDD, ANNA)(SCHWARZ, SYDNEY)(STAN, ALEX)(STAN, SARAH)(THORENSEN, ANN)(TOLKIEN, AMANDY)(WAHL, ANN)"),
                             ("Robert:Korn;James:Russell;Alex:Wahl;Alex:Steve;Sarah:Burroughs;Alexis:Stan;Sydney:Bell;John:Tolkie",
                              "(BELL, SYDNEY)(BURROUGHS, SARAH)(KORN, ROBERT)(RUSSELL, JAMES)(STAN, ALEXIS)(STEVE, ALEX)(TOLKIE, JOHN)(WAHL, ALEX)"),
                             ("Ann:Wahl;Andrew:Arno;Emily:Tolkien;Alex:Bell;Anna:Kern;Abba:Steve;Alissa:Burroughs;Antony:Schwarz;Madison:Korn;Alexis:Thorensen;John:Wah",
                              "(ARNO, ANDREW)(BELL, ALEX)(BURROUGHS, ALISSA)(KERN, ANNA)(KORN, MADISON)(SCHWARZ, ANTONY)(STEVE, ABBA)(THORENSEN, ALEXIS)(TOLKIEN, EMILY)(WAH, JOHN)(WAHL, ANN)"),
                             ("Andrew:Bell;Anna:Kern;Victoria:Schwarz;Alexis:Wahl;Amber:Arno;Sophia:Kern;Haley:Meta;Matthew:Meta;James:Gate",
                              "(ARNO, AMBER)(BELL, ANDREW)(GATE, JAMES)(KERN, ANNA)(KERN, SOPHIA)(META, HALEY)(META, MATTHEW)(SCHWARZ, VICTORIA)(WAHL, ALEXIS)"),
                             ("Haley:Gates;Elizabeth:Gates;Robert:Kern;Sarah:Bell;Anna:Wahl;Sydney:Arno;Andrew:Russell;Alex:Stan;Ann:Meta;Paul:Schwarz;Amandy:Kor",
                              "(ARNO, SYDNEY)(BELL, SARAH)(GATES, ELIZABETH)(GATES, HALEY)(KERN, ROBERT)(KOR, AMANDY)(META, ANN)(RUSSELL, ANDREW)(SCHWARZ, PAUL)(STAN, ALEX)(WAHL, ANNA)"),
                             ("Madison:Bell;Abba:Gates;Anna:Bell;Lewis:Meta;Michael:Russel;Ann:Bell;Jacob:Stan;Anna:Korn;James:Thorensen;Ann:Dorny;Paul:Meta;Emily:Kor",
                              "(BELL, ANN)(BELL, ANNA)(BELL, MADISON)(DORNY, ANN)(GATES, ABBA)(KOR, EMILY)(KORN, ANNA)(META, LEWIS)(META, PAUL)(RUSSEL, MICHAEL)(STAN, JACOB)(THORENSEN, JAMES)"),
                             ("Anna:Arno;Grace:Meta;Andrew:Korn;Antony:Dorries;Robert:Dorny;Victoria:Gates;Abba:Arno;Elizabeth:Russe",
                              "(ARNO, ABBA)(ARNO, ANNA)(DORNY, ROBERT)(DORRIES, ANTONY)(GATES, VICTORIA)(KORN, ANDREW)(META, GRACE)(RUSSE, ELIZABETH)"),
                             ("Matthew:Steve;Sophia:Cornwell;Paul:Meta;Sarah:Rudd;Ann:Kern;Victoria:Meta;Alexis:Kern;Anna:Arn",
                              "(ARN, ANNA)(CORNWELL, SOPHIA)(KERN, ALEXIS)(KERN, ANN)(META, PAUL)(META, VICTORIA)(RUDD, SARAH)(STEVE, MATTHEW)"),
                             ("Alex:Meta;Jacob:Russel;Matthew:Stan;Anna:Bell;Elizabeth:Korn;Haley:Arno;Alex:Wahl;Abba:Tolkien;Andrew:Dorries;Paul:Cornwel",
                              "(ARNO, HALEY)(BELL, ANNA)(CORNWEL, PAUL)(DORRIES, ANDREW)(KORN, ELIZABETH)(META, ALEX)(RUSSEL, JACOB)(STAN, MATTHEW)(TOLKIEN, ABBA)(WAHL, ALEX)"),
                             ("Paul:Wahl;Alex:Arno;Madison:Bell;Matthew:Rudd;Grace:Meta;Ann:Steve;Ann:Thorensen;Antony:Bel",
                              "(ARNO, ALEX)(BEL, ANTONY)(BELL, MADISON)(META, GRACE)(RUDD, MATTHEW)(STEVE, ANN)(THORENSEN, ANN)(WAHL, PAUL)"),
                             ("Alexis:Cornwell;Michael:Tolkien;Ann:Meta;Haley:Schwarz;Abba:Kern;Megan:Dorries;Alissa:Russel;Amber:Wahl;Jacob:Steve;Sydney:Russell;Paul:Cornwell;Andrew:Met",
                              "(CORNWELL, ALEXIS)(CORNWELL, PAUL)(DORRIES, MEGAN)(KERN, ABBA)(MET, ANDREW)(META, ANN)(RUSSEL, ALISSA)(RUSSELL, SYDNEY)(SCHWARZ, HALEY)(STEVE, JACOB)(TOLKIEN, MICHAEL)(WAHL, AMBER)"),
                             ("Anna:Kern;Megan:Meta;Alex:Korn;Amber:Wahl;Alexis:Russel;Alex:Gates;Ann:Meta;Emily:Kern;Ann:Schwar",
                              "(GATES, ALEX)(KERN, ANNA)(KERN, EMILY)(KORN, ALEX)(META, ANN)(META, MEGAN)(RUSSEL, ALEXIS)(SCHWAR, ANN)(WAHL, AMBER)"),
                             ("Sarah:Schwarz;Alissa:Bell;Paul:Russel;John:Steve;Elizabeth:Thorensen;Alex:Arno;Lewis:Meta;Robert:Wah",
                              "(ARNO, ALEX)(BELL, ALISSA)(META, LEWIS)(RUSSEL, PAUL)(SCHWARZ, SARAH)(STEVE, JOHN)(THORENSEN, ELIZABETH)(WAH, ROBERT)"),
                             ("Andrew:STAN;Ann:Tolkien;Matthew:Korn;Michael:Meta;Ann:Russel;Amber:Dorries;Sydney:Kern;Sarah:Rudd;Ann:Wahl;Alex:Wahl;Antony:Arno;Elizabeth:Bel",
                              "(ARNO, ANTONY)(BEL, ELIZABETH)(DORRIES, AMBER)(KERN, SYDNEY)(KORN, MATTHEW)(META, MICHAEL)(RUDD, SARAH)(RUSSEL, ANN)(STAN, ANDREW)(TOLKIEN, ANN)(WAHL, ALEX)(WAHL, ANN)"),
                             ("Alexis:Wahl;Alex:Meta;Madison:Wahl;Antony:Burroughs;Ann:Schwarz;Anna:Russel;Anna:STAN;Sarah:Cornwell;Robert:Korn;Alex:Schwarz;Haley:Ker", "(BURROUGHS, ANTONY)(CORNWELL, SARAH)(KER, HALEY)(KORN, ROBERT)(META, ALEX)(RUSSEL, ANNA)(SCHWARZ, ALEX)(SCHWARZ, ANN)(STAN, ANNA)(WAHL, ALEXIS)(WAHL, MADISON)")])
def test_random_test_cases(a, b):
    assert meeting(a) == b
