# Arquitectura es jugar

Juego de matrices para proyectar edificios con patios a diversas alturas.

## Archivos

- `index.html`: la web completa (juego, matriz, edificio 3D, parcela, catálogo, exportación y referencias).
- `referencias.json`: la galería de referencias, con sus fotos. La web la carga sola al abrirse.
- `grasshopper_casillas.py`: script para llevar `casillas.csv` a Rhino con Grasshopper.

## Cómo editar la web desde GitHub (también en iPad)

1. Abre el repositorio y toca `index.html`.
2. Toca el **lápiz** (Edit this file).
3. Busca lo que quieras cambiar. En el iPad, usa «Buscar en la página» de Safari:
   - Textos de las pantallas: busca la frase tal como aparece en la web.
   - Colores: busca `--blue`, `--paper`… al principio del archivo.
   - Valores iniciales de las reglas: busca `defaults:`.
4. Baja del todo y toca **Commit changes**. En uno o dos minutos la web publicada se actualiza.

## Cómo actualizar las referencias para todo el mundo

Las referencias que añades en la web publicada se guardan solo en tu navegador. Para que las vea cualquiera que abra el enlace:

1. En la web, ve a **Referencias** y pulsa **Exportar referencias**: se descarga `referencias.json`.
2. En GitHub, entra en el repositorio y toca **Add file › Upload files**.
3. Sube ese `referencias.json` (sustituye al anterior) y toca **Commit changes**.
