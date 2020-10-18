# scpr-coding-challenge
southern california public radio coding challenge



### Setup:

download the mongo DB daily dump for 2019-06-30 from here: `https://ghtorrent.org/downloads.html`

... this might take a few hours ...

install mongo DB if its not already installed with the command: `sudo apt-get install mongodb`

enter the mongo DB shell with the command: `mongo`

create a mongo DB database called "scpr_db" with the command: `use scpr_db`

exit the mongo DB shell with the command: `exit`

restore the downloaded daily dump with the command: `mongorestore -d scpr_db <path/to/dump/files>`

install the python libraries in requirements.txt with if not already installed: `pip3 install src/requirements.txt`

requirements.txt contains:
```
pymongo
requests
```


### Usage:

Run the following python scripts and the Solutions will be printed to the terminal:
```
python3 src/part1_bullet1.py
python3 src/part1_bullet2.py
python3 src/part1_bullet3.py
python3 src/part2_bullet1.py
python3 src/part2_bullet2.py
```

Each script takes 2-3 minutes to run, and the output should match the solutions below. See the Data_Engineer_Assessment.docx file for the orginal questions.



### Solutions:

PART 1: BULLET 1:
```
The Top 5 repos by commit activity (# of commits) are:
    1. repo https://github.com/zachwill/mario has 5475 commits.
    2. repo https://github.com/chuan12/shenzhouzd has 2606 commits.
    3. repo https://github.com/LiveChief/Most-Active-Repository has 2082 commits.
    4. repo https://github.com/gsoc-bloom-windows/ament_cmake-release has 2017 commits.
    5. repo https://github.com/geos4s/18w856162 has 1929 commits.
```

PART 1: BULLET 2:
```
The Top 5 most frequent words used in the commit messages are:
    1. word "update" occurs 119292 times.
    2. word "to" occurs 98642 times.
    3. word "add" occurs 77867 times.
    4. word "the" occurs 69206 times.
    5. word "downloading" occurs 67978 times.
```

PART 1: BULLET 3:
```
Year: 2019

    Top 5 repos of 2019 (out of 173353 total repos):
        1. repo https://github.com/zachwill/mario has 3200 commits.
        2. repo https://github.com/chuan12/shenzhouzd has 2606 commits.
        3. repo https://github.com/LiveChief/Most-Active-Repository has 2082 commits.
        4. repo https://github.com/gsoc-bloom-windows/ament_cmake-release has 2017 commits.
        5. repo https://github.com/geos4s/18w856162 has 1929 commits.

    Top 5 most frequent words of 2019 (out of 144045 total words):
        1. word "update" occurs 117504 times.
        2. word "to" occurs 87621 times.
        3. word "add" occurs 74852 times.
        4. word "downloading" occurs 67971 times.
        5. word "the" occurs 56005 times.


Year: 2018

    Top 5 repos of 2018 (out of 944 total repos):
        1. repo https://github.com/zachwill/mario has 2275 commits.
        2. repo https://github.com/ipasimulator/ipasim has 1047 commits.
        3. repo https://github.com/towers-of-hanoi/towers has 565 commits.
        4. repo https://github.com/cianixru/IAP has 388 commits.
        5. repo https://github.com/phase4ground/ka9q-radio has 307 commits.

    Top 5 most frequent words of 2018 (out of 13099 total words):
        1. word "a" occurs 4969 times.
        2. word "to" occurs 3155 times.
        3. word "the" occurs 3027 times.
        4. word "it" occurs 2975 times.
        5. word "s" occurs 2725 times.


Year: 2017

    Top 5 repos of 2017 (out of 371 total repos):
        1. repo https://github.com/GameRoomPC/GameRoom has 505 commits.
        2. repo https://github.com/phase4ground/ka9q-radio has 478 commits.
        3. repo https://github.com/qtwebkit/webkit-mirror has 417 commits.
        4. repo https://github.com/z3c-pie/kernel_sony_msm8974 has 203 commits.
        5. repo https://github.com/tmauricio80/intelligence has 197 commits.

    Top 5 most frequent words of 2017 (out of 12486 total words):
        1. word "the" occurs 3989 times.
        2. word "to" occurs 2759 times.
        3. word "a" occurs 2520 times.
        4. word "by" occurs 2483 times.
        5. word "c" occurs 1885 times.


Year: 2016

    Top 5 repos of 2016 (out of 200 total repos):
        1. repo https://github.com/wumalv/caffe-doc has 294 commits.
        2. repo https://github.com/qtwebkit/webkit-mirror has 248 commits.
        3. repo https://github.com/z3c-pie/kernel_sony_msm8974 has 229 commits.
        4. repo https://github.com/GameRoomPC/GameRoom has 196 commits.
        5. repo https://github.com/dev7788/fashion-revolution-django has 161 commits.

    Top 5 most frequent words of 2016 (out of 10502 total words):
        1. word "the" occurs 2151 times.
        2. word "to" occurs 1724 times.
        3. word "by" occurs 1522 times.
        4. word "a" occurs 1492 times.
        5. word "jsc" occurs 1431 times.


Year: 2015

    Top 5 repos of 2015 (out of 121 total repos):
        1. repo https://github.com/z3c-pie/kernel_sony_msm8974 has 239 commits.
        2. repo https://github.com/wumalv/caffe-doc has 124 commits.
        3. repo https://github.com/losnoco/foobar2000 has 104 commits.
        4. repo https://github.com/RevengeOS-Devices/android_kernel_xiaomi_land has 50 commits.
        5. repo https://github.com/SpaceRadar/STM32F4-Free-Fall-Detection has 48 commits.

    Top 5 most frequent words of 2015 (out of 4991 total words):
        1. word "the" occurs 1214 times.
        2. word "by" occurs 943 times.
        3. word "a" occurs 796 times.
        4. word "to" occurs 773 times.
        5. word "com" occurs 750 times.


Year: 2014

    Top 5 repos of 2014 (out of 87 total repos):
        1. repo https://github.com/losnoco/foobar2000 has 140 commits.
        2. repo https://github.com/wumalv/caffe-doc has 110 commits.
        3. repo https://github.com/joshuaulrich/tmp-ecfun has 86 commits.
        4. repo https://github.com/z3c-pie/kernel_sony_msm8974 has 57 commits.
        5. repo https://github.com/steam-test1/old-lua-repo has 48 commits.

    Top 5 most frequent words of 2014 (out of 3513 total words):
        1. word "the" occurs 540 times.
        2. word "by" occurs 395 times.
        3. word "to" occurs 381 times.
        4. word "d" occurs 350 times.
        5. word "svn" occurs 306 times.


Year: 2013

    Top 5 repos of 2013 (out of 70 total repos):
        1. repo https://github.com/meaganewaller/flockapp has 230 commits.
        2. repo https://github.com/losnoco/foobar2000 has 205 commits.
        3. repo https://github.com/joshuaulrich/tmp-ecdat has 121 commits.
        4. repo https://github.com/Idowuilekura/Baralicious-336 has 65 commits.
        5. repo https://github.com/psyke83/libsdl2 has 65 commits.

    Top 5 most frequent words of 2013 (out of 3589 total words):
        1. word "the" occurs 599 times.
        2. word "to" occurs 459 times.
        3. word "svn" occurs 431 times.
        4. word "d" occurs 420 times.
        5. word "a" occurs 399 times.


Year: 2012

    Top 5 repos of 2012 (out of 49 total repos):
        1. repo https://github.com/losnoco/foobar2000 has 245 commits.
        2. repo https://github.com/wso2news/robotframework has 164 commits.
        3. repo https://github.com/ipasimulator/libobjc2 has 79 commits.
        4. repo https://github.com/z3c-pie/kernel_sony_msm8974 has 57 commits.
        5. repo https://github.com/scottkillen-minecraft-textures/Isabella has 41 commits.

    Top 5 most frequent words of 2012 (out of 2934 total words):
        1. word "the" occurs 456 times.
        2. word "to" occurs 407 times.
        3. word "a" occurs 298 times.
        4. word "by" occurs 296 times.
        5. word "and" occurs 246 times.


Year: 2011

    Top 5 repos of 2011 (out of 30 total repos):
        1. repo https://github.com/wso2news/RIDE has 419 commits.
        2. repo https://github.com/ipasimulator/libobjc2 has 318 commits.
        3. repo https://github.com/losnoco/foobar2000 has 218 commits.
        4. repo https://github.com/wso2news/SwingLibrary has 132 commits.
        5. repo https://github.com/XXChester/Flowers has 64 commits.

    Top 5 most frequent words of 2011 (out of 2866 total words):
        1. word "to" occurs 547 times.
        2. word "the" occurs 538 times.
        3. word "tfs" occurs 508 times.
        4. word "c" occurs 507 times.
        5. word "id" occurs 344 times.


Year: 2010

    Top 5 repos of 2010 (out of 17 total repos):
        1. repo https://github.com/losnoco/foobar2000 has 465 commits.
        2. repo https://github.com/ipasimulator/libobjc2 has 253 commits.
        3. repo https://github.com/wso2news/SwingLibrary has 148 commits.
        4. repo https://github.com/FahadAijaz/cts-texts-arabicLit has 88 commits.
        5. repo https://github.com/losnoco/foo_midi has 50 commits.

    Top 5 most frequent words of 2010 (out of 2328 total words):
        1. word "tfs" occurs 1030 times.
        2. word "files" occurs 557 times.
        3. word "c" occurs 537 times.
        4. word "foobar" occurs 525 times.
        5. word "id" occurs 521 times.


Year: 2009

    Top 5 repos of 2009 (out of 17 total repos):
        1. repo https://github.com/wso2news/SwingLibrary has 157 commits.
        2. repo https://github.com/faizalazman/Ames-Housing-Dataset has 86 commits.
        3. repo https://github.com/korli/Beam has 64 commits.
        4. repo https://github.com/8bitpsp/vice has 50 commits.
        5. repo https://github.com/8bitpsp/fuse has 17 commits.

    Top 5 most frequent words of 2009 (out of 1260 total words):
        1. word "the" occurs 164 times.
        2. word "to" occurs 128 times.
        3. word "on" occurs 117 times.
        4. word "added" occurs 91 times.
        5. word "of" occurs 78 times.


Year: 2008

    Top 5 repos of 2008 (out of 13 total repos):
        1. repo https://github.com/wso2news/SwingLibrary has 196 commits.
        2. repo https://github.com/8bitpsp/fuse has 50 commits.
        3. repo https://github.com/qq516333132/gmenu2x-1 has 44 commits.
        4. repo https://github.com/8bitpsp/fms has 18 commits.
        5. repo https://github.com/8bitpsp/race has 18 commits.

    Top 5 most frequent words of 2008 (out of 834 total words):
        1. word "added" occurs 137 times.
        2. word "x" occurs 93 times.
        3. word "svn" occurs 89 times.
        4. word "gmenu" occurs 88 times.
        5. word "b" occurs 88 times.


Year: 2007

    Top 5 repos of 2007 (out of 8 total repos):
        1. repo https://github.com/8bitpsp/atari800 has 47 commits.
        2. repo https://github.com/8bitpsp/smsplus has 44 commits.
        3. repo https://github.com/qq516333132/gmenu2x-1 has 33 commits.
        4. repo https://github.com/8bitpsp/fms has 28 commits.
        5. repo https://github.com/8bitpsp/caprice32 has 19 commits.

    Top 5 most frequent words of 2007 (out of 672 total words):
        1. word "added" occurs 123 times.
        2. word "to" occurs 117 times.
        3. word "svn" occurs 68 times.
        4. word "x" occurs 67 times.
        5. word "gmenu" occurs 66 times.


Year: 2006

    Top 5 repos of 2006 (out of 2 total repos):
        1. repo https://github.com/qq516333132/gmenu2x-1 has 17 commits.
        2. repo https://github.com/FyiurAmron/SDL_sound has 6 commits.

    Top 5 most frequent words of 2006 (out of 91 total words):
        1. word "svn" occurs 34 times.
        2. word "gmenu" occurs 34 times.
        3. word "x" occurs 34 times.
        4. word "b" occurs 34 times.
        5. word "a" occurs 19 times.


Year: 2005

    Top 5 repos of 2005 (out of 1 total repos):
        1. repo https://github.com/FyiurAmron/SDL_sound has 17 commits.

    Top 5 most frequent words of 2005 (out of 85 total words):
        1. word "and" occurs 3 times.
        2. word "of" occurs 3 times.
        3. word "added" occurs 3 times.
        4. word "patched" occurs 3 times.
        5. word "to" occurs 3 times.


Year: 2004

    Top 5 repos of 2004 (out of 2 total repos):
        1. repo https://github.com/FyiurAmron/SDL_sound has 8 commits.
        2. repo https://github.com/Lokendraparmar/rooms.github.io has 1 commits.

    Top 5 most frequent words of 2004 (out of 228 total words):
        1. word "the" occurs 26 times.
        2. word "to" occurs 13 times.
        3. word "sound" occurs 11 times.
        4. word "we" occurs 11 times.
        5. word "this" occurs 10 times.


Year: 2003

    Top 5 repos of 2003 (out of 3 total repos):
        1. repo https://github.com/FyiurAmron/SDL_sound has 34 commits.
        2. repo https://github.com/gdsotirov/specific_defs has 5 commits.
        3. repo https://github.com/mo0z/javaDoc.vim has 2 commits.

    Top 5 most frequent words of 2003 (out of 142 total words):
        1. word "updated" occurs 15 times.
        2. word "to" occurs 8 times.
        3. word "fixed" occurs 6 times.
        4. word "add" occurs 6 times.
        5. word "timidity" occurs 5 times.


Year: 2002

    Top 5 repos of 2002 (out of 3 total repos):
        1. repo https://github.com/FyiurAmron/SDL_sound has 244 commits.
        2. repo https://github.com/paracycle/Code has 20 commits.
        3. repo https://github.com/paracycle/VSS has 20 commits.

    Top 5 most frequent words of 2002 (out of 460 total words):
        1. word "updated" occurs 89 times.
        2. word "to" occurs 50 times.
        3. word "added" occurs 35 times.
        4. word "and" occurs 31 times.
        5. word "fixed" occurs 23 times.


Year: 2001

    Top 5 repos of 2001 (out of 4 total repos):
        1. repo https://github.com/FyiurAmron/SDL_sound has 158 commits.
        2. repo https://github.com/paracycle/VSS has 87 commits.
        3. repo https://github.com/ArbitraryFox/Shinsoo_Pie has 1 commits.
        4. repo https://github.com/gdsotirov/specific_defs has 1 commits.

    Top 5 most frequent words of 2001 (out of 540 total words):
        1. word "the" occurs 96 times.
        2. word "to" occurs 60 times.
        3. word "and" occurs 56 times.
        4. word "updated" occurs 49 times.
        5. word "a" occurs 42 times.
```

PART 2: BULLET 1:
```
	Commit activity of the year 2020:

	    4  commits occured in the week of   2019/12/29 - 2020/01/04   on the days: [0, 0, 0, 2, 1, 1, 0]
	    2  commits occured in the week of   2020/01/05 - 2020/01/11   on the days: [0, 2, 0, 0, 0, 0, 0]
	    0  commits occured in the week of   2020/01/12 - 2020/01/18   on the days: [0, 0, 0, 0, 0, 0, 0]
	    0  commits occured in the week of   2020/01/19 - 2020/01/25   on the days: [0, 0, 0, 0, 0, 0, 0]
	    1  commit  occured in the week of   2020/01/26 - 2020/02/01   on the days: [1, 0, 0, 0, 0, 0, 0]
	    3  commits occured in the week of   2020/02/02 - 2020/02/08   on the days: [0, 0, 0, 2, 0, 1, 0]
	    5  commits occured in the week of   2020/02/09 - 2020/02/15   on the days: [0, 0, 5, 0, 0, 0, 0]
	    0  commits occured in the week of   2020/02/16 - 2020/02/22   on the days: [0, 0, 0, 0, 0, 0, 0]
	    1  commit  occured in the week of   2020/02/23 - 2020/02/29   on the days: [0, 0, 0, 0, 1, 0, 0]
	    1  commit  occured in the week of   2020/03/01 - 2020/03/07   on the days: [0, 0, 0, 0, 0, 1, 0]
	    4  commits occured in the week of   2020/03/08 - 2020/03/14   on the days: [0, 3, 1, 0, 0, 0, 0]
	    0  commits occured in the week of   2020/03/15 - 2020/03/21   on the days: [0, 0, 0, 0, 0, 0, 0]
	    0  commits occured in the week of   2020/03/22 - 2020/03/28   on the days: [0, 0, 0, 0, 0, 0, 0]
	    2  commits occured in the week of   2020/03/29 - 2020/04/04   on the days: [0, 1, 1, 0, 0, 0, 0]
	    3  commits occured in the week of   2020/04/05 - 2020/04/11   on the days: [0, 0, 3, 0, 0, 0, 0]
	    0  commits occured in the week of   2020/04/12 - 2020/04/18   on the days: [0, 0, 0, 0, 0, 0, 0]
	    0  commits occured in the week of   2020/04/19 - 2020/04/25   on the days: [0, 0, 0, 0, 0, 0, 0]
	    2  commits occured in the week of   2020/04/26 - 2020/05/02   on the days: [1, 0, 0, 0, 0, 1, 0]
	    0  commits occured in the week of   2020/05/03 - 2020/05/09   on the days: [0, 0, 0, 0, 0, 0, 0]
	    0  commits occured in the week of   2020/05/10 - 2020/05/16   on the days: [0, 0, 0, 0, 0, 0, 0]
	    0  commits occured in the week of   2020/05/17 - 2020/05/23   on the days: [0, 0, 0, 0, 0, 0, 0]
	    0  commits occured in the week of   2020/05/24 - 2020/05/30   on the days: [0, 0, 0, 0, 0, 0, 0]
	    4  commits occured in the week of   2020/05/31 - 2020/06/06   on the days: [0, 0, 1, 3, 0, 0, 0]
	    0  commits occured in the week of   2020/06/07 - 2020/06/13   on the days: [0, 0, 0, 0, 0, 0, 0]
	    0  commits occured in the week of   2020/06/14 - 2020/06/20   on the days: [0, 0, 0, 0, 0, 0, 0]
	    0  commits occured in the week of   2020/06/21 - 2020/06/27   on the days: [0, 0, 0, 0, 0, 0, 0]
	    1  commit  occured in the week of   2020/06/28 - 2020/07/04   on the days: [0, 0, 0, 1, 0, 0, 0]
	    0  commits occured in the week of   2020/07/05 - 2020/07/11   on the days: [0, 0, 0, 0, 0, 0, 0]
	    0  commits occured in the week of   2020/07/12 - 2020/07/18   on the days: [0, 0, 0, 0, 0, 0, 0]
	    0  commits occured in the week of   2020/07/19 - 2020/07/25   on the days: [0, 0, 0, 0, 0, 0, 0]
	    1  commit  occured in the week of   2020/07/26 - 2020/08/01   on the days: [0, 0, 0, 0, 1, 0, 0]
	    3  commits occured in the week of   2020/08/02 - 2020/08/08   on the days: [0, 0, 0, 2, 0, 1, 0]
	    2  commits occured in the week of   2020/08/09 - 2020/08/15   on the days: [0, 1, 0, 0, 1, 0, 0]
	    2  commits occured in the week of   2020/08/16 - 2020/08/22   on the days: [0, 0, 0, 0, 2, 0, 0]
	    1  commit  occured in the week of   2020/08/23 - 2020/08/29   on the days: [0, 0, 0, 1, 0, 0, 0]
	    0  commits occured in the week of   2020/08/30 - 2020/09/05   on the days: [0, 0, 0, 0, 0, 0, 0]
	    1  commit  occured in the week of   2020/09/06 - 2020/09/12   on the days: [0, 1, 0, 0, 0, 0, 0]
	    1  commit  occured in the week of   2020/09/13 - 2020/09/19   on the days: [0, 0, 0, 1, 0, 0, 0]
	    9  commits occured in the week of   2020/09/20 - 2020/09/26   on the days: [0, 9, 0, 0, 0, 0, 0]
	    1  commit  occured in the week of   2020/09/27 - 2020/10/03   on the days: [0, 0, 0, 0, 0, 1, 0]
	    2  commits occured in the week of   2020/10/04 - 2020/10/10   on the days: [0, 2, 0, 0, 0, 0, 0]
	    1  commit  occured in the week of   2020/10/11 - 2020/10/17   on the days: [0, 0, 0, 0, 0, 1, 0]
```

PART 2: BULLET 2:
```
Most active contributor in terms of commits:
    Username:    yyx990803
    Profile URL: https://github.com/yyx990803
```


