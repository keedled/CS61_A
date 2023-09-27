(define (over-or-under num1 num2)
  (cond
    ((> num1 num2) 1)
    ((< num1 num2) -1)
    (else 0))
)

;;; Tests
(over-or-under 1 2)
; expect -1
(over-or-under 2 1)
; expect 1
(over-or-under 1 1)
; expect 0


(define (filter-lst fn lst)
  (if (null? lst)
    '()
    (if (fn (car lst))
      (cons (car lst) (filter-lst fn (cdr lst)))
      (filter-lst fn (cdr lst))
      )
    )
)

;;; Tests
(define (even? x)
  (= (modulo x 2) 0))
(filter-lst even? '(0 1 1 2 3 5 8))
; expect (0 2 8)


(define (make-adder num)
  (define (make-adder_2 inc) (+ inc num))
    make-adder_2
)

;;; Tests
(define adder (make-adder 5))
(adder 8)
; expect 13


(define lst
  (list (list 1) 2 (list 3 4) 5)
)


(define (composed f g)
  (define (h x)
          (f (g x))
    )
  h
)


(define (remove item lst)
    (if (null? lst)
      '()
        (if (= item (car lst))
            (remove item (cdr lst))
            (cons (car lst) (remove item (cdr lst)))
        )
    )
)
;(define (remove item lst)
;	(if (null? lst)
;    ()
;		(if (= item (car lst))
;			(remove item (cdr lst))
;			(cons (car lst) (remove item (cdr lst)))
;		)
;	)
;)


;;; Tests
(remove 3 nil)
; expect ()
(remove 3 '(1 3 5))
; expect (1 5)
(remove 5 '(5 3 5 5 1 4 5 4))
; expect (3 1 4 4)


(define (no-repeats s)
  (if (null? s)
  '()
  (cons (car s) (no-repeats(remove (car s) (cdr s))))
    )
)


(define (substitute s old new)
  (if (null? s)
    '()
    (cond
      ((pair? (car s)) (cons (substitute (car s) old new) (substitute (cdr s) old new) ))
      ((eq? old (car s)) (cons new (substitute (cdr s) old new)))
      (else
        (cons (car s) (substitute (cdr s) old new))
    ))
    )
  )

;(define (sub-all s olds news)
;	(if (null? s) nil
;		(if (null? olds) s
;		(sub-all (substitute s (car olds) (car news)) (cdr olds) (cdr news))
;		)
;	)
;)

(define (sub-all s olds news)
  (if (null? s) nil
    (if (null? olds) s
    (sub-all (substitute s (car olds) (car news)) (cdr olds) (cdr news))
      )
    )
)

