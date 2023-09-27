(define (split-at lst n)
	(define (get_index sub_lst res_lst index)
		(if (null? res_lst)
			(cons sub_lst nil)
		(if (= index n)
			(cons sub_lst res_lst)
			(get_index (append sub_lst (list (car res_lst))) (cdr res_lst) (+ 1 index))
				)
			)
		)
	(get_index '() lst 0)
)


(define-macro (switch expr cases)
	(cons 'cond
		(map (lambda (case) (cons (eq? (eval expr) (car case)) (cdr case)))
    			cases))
)


;(define-macro (switch expr cases)
;	 (cons 'cond
;	   (map (lambda (case) (cons (eq? (eval expr) (car case)) (cdr case)))
;    			cases))
;)