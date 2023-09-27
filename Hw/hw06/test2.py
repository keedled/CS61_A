from hw06 import Tree,Link
def deep_map(f, link):
    # """Return a Link with the same structure as link but with fn mapped over
    # its elements. If an element is an instance of a linked list, recursively
    # apply f inside that linked list as well.
    #
    # >>> s = Link(1, Link(Link(2, Link(3)), Link(4)))
    # >>> print(deep_map(lambda x: x * x, s))
    # <1 <4 9> 16>
    # >>> print(s) # unchanged
    # <1 <2 3> 4>
    # >>> print(deep_map(lambda x: 2 * x, Link(s, Link(Link(Link(5))))))
    # <<2 <4 6> 8> <<10>>>
    # """
    "*** YOUR CODE HERE ***"
    def copy_Link(l):
        if l == Link.empty:
            return Link.empty
        if type(l.first) == Link:
            l_t = Link(copy_Link(l.first))
        else:
            l_t = Link(l.first)
        l_t.rest = copy_Link(l.rest)
        return l_t
    link_t = copy_Link(link)
    def deep_map_helper(f,link_t):
        while link_t.rest is not Link.empty:
            if type(link_t.first) == Link:
                deep_map_helper(f,link_t.first)
            else:
                link_t.first = f(link_t.first)
            link_t = link_t.rest

        if type(link_t.first) == Link:
            deep_map_helper(f,link_t.first)
        else:
            link_t.first = f(link_t.first)

    deep_map_helper(f,link_t)
    return link_t
s = Link(1, Link(Link(2, Link(3)), Link(4)))
print(deep_map(lambda x: x * x, s))
print(s)