import graphviz



s = graphviz.Digraph('Tabla', filename='MAINS/Reportes/Tabla.pdf',
                     node_attr={'shape': 'plaintext'})

table_content = '''<
<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0">  <TR>
                        <TD>REPORTE MBR</TD>
                        <TD>    </TD>
                    </TR>
                    <TR>
                        <TD>mbr_tamaño:</TD>
                        <TD>12582912</TD>
                    </TR>
                    <TR>
                        <TD>mbr_fecha_creacion:</TD>
                        <TD>2023-09-14 18:55:41</TD>
                    </TR>
                    <TR>
                        <TD>mbr_disk_signature:</TD>
                        <TD>197</TD>
                    </TR>
                    
                    
                    
        </TABLE>>'''

s.node('struct1', table_content)
s.view()
# print(s)