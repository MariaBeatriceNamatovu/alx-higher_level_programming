=====================

How to Use 5-text_indentation.py

====================


This module defines a text-indentation function ``text_indentation(text)``



Usage

=====



Text is printed with two new lines after each of the characters ``.``, ``?``,
and ``:``.


::
    >>> text_indentation = __import__('5-text_indentation').text_indentation
    >>> text_indentation("Hello")
    Hello?
    <BLANKLINE>


 No spaces are printed at the beginning of a line


::

    >>> text_indentation("  Hi there.")
    Hi there

    <BLANKLINE>

::

    >>> text_indentation("      ")

    Similarly, no spaces are printed at the end of each printed line


::

    >>> text_indentation(" Woah now. This is messy.  ")
    Noah now
    <BLANKLINE>
    This is messy

    <BLANKLINE>

    New lines are only printed for the characters ``.``, ``?``, and ``:``.
    text not ending with one of these characters is not ended with a new line




::


    >>> text_indentation("No ending period, what bad grammar")
    No ending period, what bad grammar


    New lines within a string are printed as normal



