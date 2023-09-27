(define (cddr s)
  (cdr (cdr s)))

(define (cadr s)
  (car (cdr s))
  )

(define (caddr s)
  (car (cddr s))
)


(define (sign num)
  (cond
    ((> num 0) 1 )
    ((< num 0) -1 )
    (else 0)
    )
)


(define (square x) (* x x))

(define (pow x y)
  (cond
    ((= 1 y) x)
    ((even? y) (pow (square x) (/ y 2)))
    ((odd? y) (* x (pow (square x) (/ (- y 1) 2))))
    )
)


(define (unique s)
    'YOUR-CODE-HERE
    (if (null? s) nil
        (cons (car s) (unique (filter (lambda (x) (not (eq? x (car s)))) (cdr s)))))
)

;(define (replicate x n)
;	(if (= n 0)
;		nil
;		(cons x
;      (replicate x (- n 1) )
;      )
;    )
;  )

;(define (replicate x n)
;    (define (rep_help x n s)
;        (if (= n 0) s
;            (rep_help x (- n 1) (cons x s))
;        )
;    )
;    (rep_help x n nil)
;)

(define (replicate x n)
  (define (helper lst x n)
    (if (= n 0) lst
                 (helper (cons x lst) x (- n 1))

      )
    )
  (helper () x n)
  )

(define (accumulate combiner start n term)
  (define
    (helper n term index res)
    (if (> index n)
        res
        (helper n term (+ index 1) (combiner res (term index)) )
      )
    )
  (helper n term 1 start)
  )


(define (accumulate-tail combiner start n term)
  (define
    (helper n term index res)
    (if (> index n)
        res
        (helper n term (+ index 1) (combiner res (term index)) )
      )
    )
  (helper n term 1 start)
)


(define-macro
 (list-of map-expr for var in lst if filter-expr)
; 'YOUR-CODE-HERE
  `(map (lambda (,var) ,map-expr) (filter (lambda (,var) ,filter-expr) ,lst) )
;  `(map (lambda (,var) ,map-expr) (filter (lambda (,var) ,filter-expr) ,lst))
)