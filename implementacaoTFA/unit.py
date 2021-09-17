'''
Testes unitários para as implementações
pip install pytest
Rodar com "$pytest unit.py"
Windows: py -m pytest unit.py
'''

import exemplos.prop_lr as prop_lr_exp
import tc.prop_lr as prop_lr
import exemplos.afd_m1 as exp


def test_tfa_table():
    
    assert prop_lr.tfa_table(exp.M1) == \
        [
            ['q1', 'q2', ''],
            ['q1', 'q3', ''],
            ['q2', 'q3', ''],
        ]
    
    assert prop_lr.tfa_table(prop_lr_exp.automato) == \
        [
            ['q0', 'q1', ''],
            ['q0', 'q2', ''],
            ['q0', 'q3', ''],
            ['q0', 'q4', ''],
            ['q0', 'q5', ''],
            ['q1', 'q2', ''],
            ['q1', 'q3', ''],
            ['q1', 'q4', ''],
            ['q1', 'q5', ''],
            ['q2', 'q3', ''],
            ['q2', 'q4', ''],
            ['q2', 'q5', ''],
            ['q3', 'q4', ''],
            ['q3', 'q5', ''],
            ['q4', 'q5', '']
        ]
    

def test_tfa_fill():
    
    assert prop_lr.tfa_fill(exp.M1) == \
        [
            ['q1', 'q2', 'd'],
            ['q1', 'q3', 'i'],
            ['q2', 'q3', 'd'],
        ]

    assert prop_lr.tfa_fill(prop_lr_exp.automato) == \
        [
            ['q0', 'q1', 'd'],
            ['q0', 'q2', 'd'],
            ['q0', 'q3', 'd'],
            ['q0', 'q4', 'd'],
            ['q0', 'q5', 'd'],
            ['q1', 'q2', 'd'],
            ['q1', 'q3', 'd'],
            ['q1', 'q4', 'd'],
            ['q1', 'q5', 'd'],
            ['q2', 'q3', 'i'],
            ['q2', 'q4', 'd'],
            ['q2', 'q5', 'd'],
            ['q3', 'q4', 'd'],
            ['q3', 'q5', 'd'],
            ['q4', 'q5', 'i']
        ]

