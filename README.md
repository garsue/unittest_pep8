unittest runner with pep8
=========================


About
-----

This script is Python unittest runner. Check the pep8 at the same time.


Basic Usage
-----------

Make testsuite directory and put test cases in it.

Then run `python runtests.py [option]`.


Options
-------

* `--report`: Generate xml report. This option depends on *unittest-xml-reporting*.
* `--without-pep8`: Run tests without pep8 checking.
* `--pattern <pettern>`: Pattern to match test files (‘test\*.py’ default)


Referenced Code
---------------

[2010 09 20 Pythonのコーディング規約pep8チェックをUnitTestに組み込んでみた - 清水川Web][1]


[1]: http://www.freia.jp/taka/blog/736/index.html   '2010 09 20 Pythonのコーディング規約pep8チェックをUnitTestに組み込んでみた - 清水川Web'
