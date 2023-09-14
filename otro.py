import graphviz

s = graphviz.Digraph('Tabla', filename='Reportes/Tabla.pdf',
                     node_attr={'shape': 'plaintext'})

table_content = '''<
<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0">
  <TR>
    <TD>left</TD>
    <TD>middle</TD>
  </TR>
   <TR>
    <TD>left</TD>
    <TD>middle</TD>
  </TR>
</TABLE>>'''

s.node('struct1', table_content)
s.view()