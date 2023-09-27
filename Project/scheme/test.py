from scheme_reader import *
from scheme import *

#do_cond_form(read_line("((#f (print 2)) (#t 3))"),)
do_let_form(read_line("(((x 2) (y 3)) (+ x y))"),  create_global_frame())