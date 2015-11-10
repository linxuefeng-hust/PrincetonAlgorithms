"""Immutable weighted directed edge."""

 #  For additional documentation, see <a href="http://algs4.cs.princeton.edu/44sp">Section 4.4</a> of
 #  <i>Algorithms, 4th Edition</i> by Robert Sedgewick and Kevin Wayne.

class DirectedEdge(object): 
  """a directed edge from vertex v to vertex w with the given weight"""

  def __init__(self, v, w, weight):
    if v < 0: raise Exception("Vertex names must be nonnegative integers")
    if w < 0: raise Exception("Vertex names must be nonnegative integers")
    if Double.isNaN(weight): raise new IllegalArgumentException("Weight is NaN")
    self._v = v # the tail vertex
    self._w = w # the head vertex
    self._weight = weight # the weight of the directed edge

  def from(self): return self._v # Returns the tail vertex of the directed edge.
  def to(self): return self._w # Returns the head vertex of the directed edge.
  def weight(self): return self._weight # Returns the weight of the directed edge.
  def __str__(self):
    return "{v} -> {w} {wt:5.2f}".format(v=self._v, w=self._w, wt=self._weight)

# Copyright 2002-2015, Robert Sedgewick and Kevin Wayne.
# Copyright 2015-2016, DV Klopfenstein, Python port
