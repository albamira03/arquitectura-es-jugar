# Arquitectura es jugar: de casillas.csv a volúmenes en Rhino
# Entradas: ruta (str) y por_plantas (bool)
# Salidas: volumenes, plantas, tipos, jugadores
import io, math
import Rhino.Geometry as rg

try:
    por_plantas = bool(por_plantas)
except NameError:
    por_plantas = False

volumenes, plantas, tipos, jugadores = [], [], [], []
with io.open(ruta, encoding='utf-8-sig') as f:
    lineas = f.read().splitlines()
cab = lineas[0].split(',')
col = dict((nombre, i) for i, nombre in enumerate(cab))

for linea in lineas[1:]:
    c = linea.split(',')
    if len(c) < len(cab):
        continue
    n = int(float(c[col['plantas']]))
    if n <= 0:
        continue
    x = float(c[col['x_m']]); y = float(c[col['y_m']])
    w = float(c[col['ancho_m']]); d = float(c[col['fondo_m']])
    giro = math.radians(float(c[col['giro_grados']]))
    alto = float(c[col['altura_m']]) / n
    if 'celda' in col and c[col['celda']] == 'hexagono':
        pts = [rg.Point3d(x + w * 0.57735 * math.sin(k * math.pi / 3),
                          y - d * 0.57735 * math.cos(k * math.pi / 3), 0) for k in range(7)]
        base = rg.PolylineCurve(pts)
    else:
        pl = rg.Plane(rg.Point3d(x, y, 0), rg.Vector3d.ZAxis)
        pl.Rotate(giro, rg.Vector3d.ZAxis)
        base = rg.Rectangle3d(pl, rg.Interval(-w / 2, w / 2), rg.Interval(-d / 2, d / 2)).ToNurbsCurve()
    pisos = range(n) if por_plantas else [0]
    for k in pisos:
        h = alto if por_plantas else alto * n
        crv = base.DuplicateCurve()
        crv.Translate(rg.Vector3d(0, 0, k * alto))
        brep = rg.Surface.CreateExtrusion(crv, rg.Vector3d(0, 0, h)).ToBrep().CapPlanarHoles(0.001)
        volumenes.append(brep)
        plantas.append(k + 1 if por_plantas else n)
        tipos.append(c[col['tipo']])
        jugadores.append(c[col['jugador']])
