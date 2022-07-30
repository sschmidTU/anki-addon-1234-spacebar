#!/usr/bin/env python
# -*- coding: utf-8 -*-

# anki-space-behaviour
# Copyright (C) @viql

from aqt.reviewer import Reviewer
from aqt import mw
from typing import Literal

config = mw.addonManager.getConfig(__name__)

oldAnswerCard = Reviewer._answerCard

def newAnswerCard(self, ease: Literal[1, 2, 3, 4]) -> None:
    #if self.state == "answer" and config.get("mode") == "show_answer":
    if self.state != "answer":
        self._showAnswer()
        return
    oldAnswerCard(self, ease)

Reviewer._answerCard = newAnswerCard