# -*- coding: utf-8 -*-

ldlf_formulas = [
    "tt",
    "ff",
    "!tt",
    "!ff",
    "tt & tt",
    "tt & ff",
    "ff & ff",
    "tt | ff",
    "tt | ff",
    "<true>tt",
    "<true>ff",
    "[true]tt",
    "[true]ff",
    "<A>tt",
    "<A>ff",
    "[A]tt",
    "[A]ff",
    "<A & B>tt",
    "<A & B>ff",
    "<A | C>tt",
    "<A | C>ff",
    "<A + B>tt",
    "<A + B>ff",
    "<A ; B>tt",
    "<A ; B>ff",
    "<A*>tt",
    "<A*>ff",
    "<<A>tt?>tt",
    "<<A>tt?>ff",
    "[A & B]tt",
    "[A & B]ff",
    "[A | C]tt",
    "[A | C]ff",
    "[A + B]tt",
    "[A + B]ff",
    "[A ; B]tt",
    "[A ; B]ff",
    "[A*]tt",
    "[A*]ff",
    "[<A>tt?]tt",
    "[<A>tt?]ff",
]


ltlf_formulas = [
    "A",
    "!A",
    "A | B",
    "A & B",
    "X A",
    "WX A",
    "A U B",
    "A R B",
    "F A",
    "G A",
    "F(G(A))",
    "G(F(A))",
    "G(true)",
    "F(true)",
    "G(false)",
    "F(false)",
    "last",
    "end",
    "true",
    "false",
    "A -> B",
    "A <-> B",
    "G(A -> B)",
    "G(A -> F(B))",
    "G(A -> B -> C)",
]