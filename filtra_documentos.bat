@echo off
setlocal
echo ################################################
echo ############   DOCUMENTS FILTER  ###############
echo #################   rubengb   ##################
echo.
echo.

rem Obtener el nombre del archivo y la palabra clave del usuario
set /p nombre_archivo="Introduce el nombre completo del fichero con extension: "
set /p palabra_clave="Introduce la palabra clave: "

rem Ejecutar el script de Python
python src/busca_logs.py "%nombre_archivo%" "%palabra_clave%"

echo.
echo.
echo Busqueda finalizada. Presiona una tecla para cerrar...
pause >nul

endlocal