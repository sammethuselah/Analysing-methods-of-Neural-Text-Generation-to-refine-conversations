#!/usr/bin/env python3

# Copyright (c) Facebook, Inc. and its affiliates.
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

from parlai.utils.testing import AutoTeacherTest


class TestDefaultTeacher(AutoTeacherTest):
    task = "safety_mix"


class TestPosSafetyMixTeacher(AutoTeacherTest):
    task = "safety_mix:PosSafetyMixTeacher"


class TestNegSafetyMixTeacher(AutoTeacherTest):
    task = "safety_mix:NegSafetyMixTeacher"
