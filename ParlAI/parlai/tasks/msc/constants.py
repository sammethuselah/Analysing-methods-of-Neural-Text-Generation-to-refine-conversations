#!/usr/bin/env python3

# Copyright (c) Facebook, Inc. and its affiliates.
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.


INITIAL_DATA_TO_COMPLETE = [
    'valid_0',
    'valid_1',
    'valid_10',
    'valid_100',
    'valid_101',
    'valid_102',
    'valid_103',
    'valid_105',
    'valid_106',
    'valid_107',
    'valid_108',
    'valid_109',
    'valid_11',
    'valid_110',
    'valid_111',
    'valid_112',
    'valid_115',
    'valid_116',
    'valid_117',
    'valid_119',
    'valid_12',
    'valid_120',
    'valid_121',
    'valid_122',
    'valid_123',
    'valid_124',
    'valid_125',
    'valid_13',
    'valid_130',
    'valid_131',
    'valid_133',
    'valid_136',
    'valid_138',
    'valid_139',
    'valid_14',
    'valid_140',
    'valid_141',
    'valid_143',
    'valid_144',
    'valid_145',
    'valid_146',
    'valid_147',
    'valid_148',
    'valid_15',
    'valid_152',
    'valid_153',
    'valid_154',
    'valid_155',
    'valid_156',
    'valid_158',
    'valid_160',
    'valid_162',
    'valid_163',
    'valid_166',
    'valid_169',
    'valid_17',
    'valid_171',
    'valid_172',
    'valid_174',
    'valid_175',
    'valid_176',
    'valid_177',
    'valid_178',
    'valid_18',
    'valid_181',
    'valid_182',
    'valid_184',
    'valid_187',
    'valid_19',
    'valid_190',
    'valid_191',
    'valid_192',
    'valid_193',
    'valid_194',
    'valid_196',
    'valid_2',
    'valid_20',
    'valid_202',
    'valid_203',
    'valid_205',
    'valid_206',
    'valid_207',
    'valid_208',
    'valid_212',
    'valid_214',
    'valid_215',
    'valid_216',
    'valid_217',
    'valid_219',
    'valid_223',
    'valid_225',
    'valid_227',
    'valid_228',
    'valid_23',
    'valid_230',
    'valid_231',
    'valid_232',
    'valid_233',
    'valid_234',
    'valid_236',
]

COMMON_CONFIG = {
    'task': 'msc:SessionBaseMsc',
    'num_examples': -1,
    'label_speaker_id': 'their',
    'session_id': 4,
    'datatype': 'valid',
}

MODEL_OPT = {
    'BST90M': {
        'previous_persona_type': 'none',
        'num_previous_sessions_msg': 10,
        'include_time_gap': False,
    }
}

UI_OPT = {'BST90M': {'previous_persona_type': 'both', 'include_time_gap': False}}
