<center>

[comment]: <img src="./media/media/image1.png" style="width:1.088in;height:1.46256in" alt="escudo.png" />

![./media/media/image1.png](./media/logo-upt.png)

**UNIVERSIDAD PRIVADA DE TACNA**

**FACULTAD DE INGENIERIA**

**Escuela Profesional de Ingeniería de Sistemas**


**Plataforma de Colaboración Académica para Proyectos Innovadores en Ingeniería de Sistemas**

Curso: **Patrones de Software**

Docente: **Mag. Patrick José Cuadros Quiroga**

**Integrantes:**

Brian Danilo Chite Quispe (2021070015)

Piero Alexander Paja de la Cruz (2020067576)

Mary Luz Chura Ticona (2019065163)

**Tacna – Perú**

**2025**

 

</center>
<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

|CONTROL DE VERSIONES||||||
| :-: | :- | :- | :- | :- | :- |
|Versión|Hecha por|Revisada por|Aprobada por|Fecha|Motivo|
|1\.0|MPV|ELV|ARV|10/10/2020|Versión Original|



**Sistema Plataforma de Colaboración Académica para Proyectos Innovadores en Ingeniería de Sistemas**

**Documento de Visión**

**Versión {1.0}**

<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

|CONTROL DE VERSIONES||||||
| :-: | :- | :- | :- | :- | :- |
|Versión|Hecha por|Revisada por|Aprobada por|Fecha|Motivo|
|1\.0|MPV|ELV|ARV|2/05/2025|Versión Original|



1. **Introducción**

   1. **Propósito**

    El propósito es desarrollar una Plataforma de Colaboración Académica para Proyectos Innovadores en Ingeniería de Sistemas, facilitando la interacción entre estudiantes, docentes e investigadores. La plataforma permitirá compartir conocimientos, gestionar proyectos colaborativos y fomentar la innovación en el ámbito de la Ingeniería de Sistemas.

    2. **Alcance**

   Este informe abarca el desarrollo y funcionalidad de la Plataforma de Colaboración Académica para Proyectos Innovadores en Ingeniería de Sistemas. Se tratarán los siguientes puntos:

    - Características y herramientas de la plataforma para la gestión de proyectos colaborativos.
    - Tipos de usuarios que participarán (estudiantes, docentes e investigadores).
    - Funcionalidades para compartir conocimientos y recursos académicos.
    - Beneficios esperados en la formación académica y en la innovación en Ingeniería de Sistemas.

    3. **Definición, Siglas y Abreviaturas**

        **PCAPIIS**: Plataforma de Colaboración Académica para Proyectos Innovadores en Ingeniería de Sistemas. Sistema diseñado para facilitar la interacción y el trabajo colaborativo en el ámbito académico.
    
        **Proyecto Innovador**: Iniciativa académica o de investigación que busca desarrollar soluciones tecnológicas novedosas en Ingeniería de Sistemas.
    
        **Usuario**: Persona registrada en la plataforma, pudiendo ser estudiante, docente o investigador.
    
        **Repositorio de Conocimiento**: Espacio dentro de la plataforma donde los usuarios pueden compartir documentos, artículos, códigos y otros recursos académicos.

        **Gestión de Proyectos**: Conjunto de herramientas y funcionalidades de la plataforma que permiten la planificación, seguimiento y colaboración en proyectos académicos.**



    4. **Referencias**

        Los documentos que se van a utilizar como referencia serán los siguientes:

        - Documento de Especificación de Requerimientos – SRS 
        - Documento de Arquitectura de Software – SAD
        - Documento de Informe de Factibilidad

    5. **Visión General**

        Este documento describe el propósito, alcance, características y restricciones de la Plataforma de Colaboración Académica para Proyectos Innovadores en Ingeniería de Sistemas, junto con los perfiles de los usuarios involucrados y las funcionalidades requeridas para facilitar la gestión y desarrollo de proyectos colaborativos en el ámbito académico.

    6. **Posicionamiento**

        1. **Oportunidad de negocio**

        La implementación de la Plataforma de Colaboración Académica para Proyectos Innovadores en Ingeniería de Sistemas representa una oportunidad para fortalecer la interacción entre estudiantes, docentes e investigadores, fomentando el desarrollo de proyectos innovadores. Además, permite mejorar la formación académica mediante el aprendizaje colaborativo y la gestión eficiente de conocimientos. Esta iniciativa puede posicionar a la institución como un referente en la innovación académica, atrayendo nuevos estudiantes y facilitando la vinculación con empresas e instituciones interesadas en el talento y la investigación en Ingeniería de Sistemas.

        2. **Definición del problema**

        Actualmente, no existe una plataforma estructurada que facilite la colaboración académica y la gestión de proyectos innovadores en Ingeniería de Sistemas. Esto dificulta la interacción entre estudiantes, docentes e investigadores, limitando el intercambio de conocimientos, la optimización de recursos y la generación de soluciones tecnológicas innovadoras. La ausencia de un espacio centralizado restringe la visibilidad de los proyectos, la formación colaborativa y la vinculación con el sector académico y empresarial.

        3. **Descripción de los interesados y usuarios**


            1. **Resumen de los interesados**

|**Interesados**|**Representante**|**Papel**|
| :- | :- | :- |
|**Brian Danilo Chite**|**Jefe de proyecto**|Responsable de la gestión y supervisión del desarrollo de la plataforma.|
|**Mary Luz Ticona**|**Analista y programador**|Responsable del diseño, desarrollo e implementación de la plataforma.|
|**Piero Paja de la Cruz**|**Analista y programador**|Responsable del desarrollo de módulos y funcionalidades específicas de la plataforma.|

****

2. **Resumen de los usuarios**

   |**Nombre**|**Descripción**|
   | :- | :- |
   |**Docentes de Ingeniería de Sistemas**|Pueden utilizar la plataforma para guiar y supervisar proyectos, compartir conocimientos y fomentar la innovación en sus áreas de especialización.|
   |**Estudiantes de Ingeniería de Sistemas**|Tendrán acceso a un espacio de colaboración donde podrán desarrollar proyectos, compartir ideas y conectarse con docentes e investigadores.|
   |**Investigadores**|Podrán compartir sus estudios, colaborar en proyectos académicos y acceder a un repositorio de conocimientos en Ingeniería de Sistemas.|
   |**Empresas y organizaciones**|Tendrán la posibilidad de conocer proyectos innovadores, identificar talento y establecer vínculos con la comunidad académica para posibles colaboraciones.|
   ****



3. **Entorno de usuario**

   La Plataforma de Colaboración Académica para Proyectos Innovadores en Ingeniería de Sistemas estará dirigida a diversos actores dentro y fuera del ámbito académico. Será utilizada por estudiantes, docentes e investigadores para gestionar y desarrollar proyectos colaborativos, así como por empresas e instituciones interesadas en la innovación tecnológica y la vinculación con la comunidad académica.

  ****
  
4. **Perfiles de interesados**

   |**Perfil de Interesado**||
   | :- | :- |
   |**Representante**|**Jefe de proyecto**|
   |**Descripción**|**Encargado de supervisar la gestión y desarrollo de la plataforma.**|
   |**Tipo**|**Líder del proyecto**|
   |**Responsabilidades**|**Supervisa el avance del proyecto, garantiza el cumplimiento de los objetivos y coordina el trabajo del equipo hasta su finalización.**|
   |**Criterios**|**El éxito del proyecto se mide por su implementación dentro del tiempo estimado, la funcionalidad de la plataforma y la satisfacción de los usuarios finales.**|
   |**Implicación**|**Revisor de requisitos, supervisor del desarrollo y facilitador de recursos.**|
   |**Entregables**|**Ninguno**|
     ****

   |**Perfil de Interesado**||
   | :- | :- |
   |**Representante**|**Docentes de la EPIS**|
   |**Descripción**|**Responsables de la formación académica y orientación de los estudiantes en el desarrollo de proyectos innovadores.**|
   |**Tipo**|**Apoyo del proyecto**|
   |**Responsabilidades**|<p>**Guiar a los estudiantes en la planificación y ejecución de proyectos.**</p><p>**Facilitar conocimientos técnicos y metodológicos para el desarrollo colaborativo.**</p><p>**Fomentar la innovación y el aprendizaje basado en proyectos.**</p>|
   |**Criterios**|**Calidad de los proyectos desarrollados, impacto en la formación académica y aplicabilidad en el ámbito profesional.**|
   |**Implicación**|**Mentoría y supervisión de proyectos.**|
   |**Entregables**|**Ninguna**|
   **  ****



5. **Perfiles de usuarios**

   |**Perfil de Usuario**||
   | :- | :- |
   |**Representante**|**Estudiantes de Ingeniería de Sistemas**|
   |**Descripción**|**Futuros profesionales que buscan un espacio para desarrollar proyectos innovadores y colaborar con docentes e investigadores.**|
   |**Tipo**|**Beneficiarios**|
   |**Responsabilidades**|<p>**Participar activamente en la creación y desarrollo de proyectos.**</p><p>**Colaborar con otros estudiantes, docentes e investigadores en iniciativas académicas.**</p><p>**Adquirir experiencia práctica en la gestión y ejecución de proyectos.**</p>|
   |**Criterios**|**Accesibilidad a la plataforma, facilidad para colaborar en proyectos y efectividad en la conexión con otros actores académicos y profesionales.**|
   |**Implicación**|**Son los principales usuarios de la plataforma y beneficiarios del ecosistema de colaboración académica.**|
   |**Entregables**|**Ninguna**|
   **  ****



6. **Necesidades de los interesados y usuarios**

|**Necesidades**|**Prioridad**|**Inquietudes**|**Solución Actual**|**Solución Propuesta**|
| :- | :- | :- | :- | :- |
|Contar con un espacio de colaboración para desarrollar proyectos innovadores en Ingeniería de Sistemas.|Alta|Falta de un entorno estructurado que facilite la interacción y el desarrollo de ideas entre estudiantes, docentes e investigadores.|Uso de herramientas dispersas como correos, grupos de WhatsApp o reuniones presenciales sin seguimiento.|Creación de la *Plataforma de Colaboración Académica*, donde se centralizan proyectos, documentación y comunicación.|
|Acceder a asesoramiento y mentoría para mejorar la calidad de los proyectos.|Alta|Dificultad para obtener retroalimentación continua de docentes y expertos.|Consultas informales con docentes o búsqueda de información en línea sin orientación personalizada.|Implementación de espacios de mentoría dentro de la plataforma, con interacción estructurada entre estudiantes y docentes.|
|Compartir recursos y conocimientos entre los participantes.|Media|Falta de un repositorio centralizado de documentación, guías y experiencias de proyectos anteriores.|Almacenamiento disperso en Google Drive, GitHub o documentos individuales.|Integración de un repositorio en la plataforma para almacenar y compartir documentación relevante.|
|Difundir proyectos destacados para obtener visibilidad y oportunidades.|Alta|Proyectos con impacto académico o tecnológico quedan limitados a círculos internos sin difusión.|Presentaciones aisladas en eventos académicos o publicaciones en redes sociales personales.|Espacio dentro de la plataforma para la difusión de proyectos destacados y conexión con instituciones y empresas.|
|Facilitar la conexión entre estudiantes, docentes e investigadores de distintas áreas.|Alta|Falta de comunicación efectiva para formar equipos multidisciplinarios.|Búsqueda manual de colaboradores en redes sociales o eventos internos.|Implementación de perfiles de usuario dentro de la plataforma, con opciones de búsqueda y conexión entre miembros según intereses y habilidades.|
|Facilitar la conexión entre estudiantes, docentes e investigadores de distintas áreas.|Alta|Falta de comunicación efectiva para formar equipos multidisciplinarios.|Búsqueda manual de colaboradores en redes sociales o eventos internos.|Implementación de un sistema de búsqueda de perfiles y coincidencias dentro de la plataforma, permitiendo identificar posibles colaboradores por áreas de interés, habilidades, o experiencia previa en proyectos.|

5. **Vista General del Producto**
   
5.1. **Perspectiva del producto**

La Plataforma de Colaboración Académica para Proyectos Innovadores en Ingeniería de Sistemas (PCAPIIS) se presenta como una herramienta estratégica para potenciar la innovación y el trabajo colaborativo dentro del entorno universitario. Al centralizar la gestión de proyectos académicos y facilitar la interacción entre estudiantes, docentes y profesionales externos, esta plataforma no solo promueve la calidad en la formación académica, sino que también fortalece el vínculo entre la universidad y el entorno productivo.

Además, el sistema permitirá visibilizar los proyectos desarrollados por los estudiantes, generando una vitrina de talento que podrá ser consultada por empresas e instituciones interesadas en soluciones tecnológicas, lo que mejora la empleabilidad de los egresados y posiciona a la Escuela Profesional de Ingeniería de Sistemas (EPIS) de la UPT como un referente en formación aplicada e innovación académica.

5.2. **Resumen de capacidades**

La Plataforma de Colaboración Académica PCAPIIS está diseñada para potenciar el trabajo conjunto entre estudiantes, docentes e investigadores, brindando las siguientes capacidades clave:

- **Gestión de Proyectos Académicos**: La plataforma permitirá registrar, organizar y dar seguimiento a proyectos de investigación, trabajos colaborativos y actividades académicas, facilitando la planificación y el cumplimiento de objetivos.
- **Comunicación y Colaboración en Tiempo Real**: A través de funciones como mensajería, foros, videoconferencias y notificaciones, PCAPIIS fomentará una comunicación fluida y efectiva entre los miembros de la comunidad académica.
- **Interoperabilidad con Recursos Académicos**: Integración con bibliotecas virtuales, bases de datos científicas, y repositorios institucionales para acceder a información relevante de manera rápida y directa desde la plataforma.
- **Seguimiento del Rendimiento y Resultados**: Herramientas analíticas para evaluar la participación, el avance de los proyectos y la producción académica, permitiendo la generación de reportes e indicadores clave para la toma de decisiones.
- **Entorno Personalizado y Seguro**: Cada usuario tendrá un perfil adaptado a su rol (estudiante, docente, investigador), con acceso seguro a sus contenidos, historial de colaboración y materiales compartidos.

5.3. **Suposiciones y dependencias:**

1. **Disponibilidad de Conectividad y Acceso a Internet**: Se asume que los usuarios (docentes, estudiantes, investigadores) contarán con acceso estable a Internet para utilizar la plataforma en sus actividades académicas diarias.
1. **Participación Activa de la Comunidad Académica**: Se asume que los actores clave de la universidad estarán dispuestos a utilizar la plataforma de manera activa, registrando proyectos, compartiendo recursos y participando en espacios de colaboración.
1. **Soporte Institucional y Técnico**: El éxito del proyecto depende del respaldo institucional de la universidad, así como del soporte técnico continuo para el mantenimiento, mejora y resolución de problemas en la plataforma.
1. **Acceso a Recursos Digitales Académicos**: La funcionalidad de interoperabilidad dependerá de la disponibilidad y acceso a bibliotecas virtuales, bases de datos científicas y otros repositorios académicos con los que la plataforma se integrará.
1. **Cumplimiento de Políticas de Seguridad y Privacidad**: Se asume que el uso de la plataforma respetará las políticas institucionales sobre protección de datos personales, asegurando la privacidad de los usuarios y la confidencialidad de los contenidos académicos compartidos.
6. **Costos y precios**

   El proyecto se basa en tecnologías y herramientas de bajo costo, lo que permite su implementación sin requerir grandes inversiones iniciales. La mayor inversión se centrará en el desarrollo de la plataforma, la integración de servicios, y la capacitación del personal encargado de su gestión y mantenimiento. La infraestructura tecnológica necesaria, como servidores y bases de datos, puede ser gestionada utilizando soluciones de código abierto o de bajo costo, y los recursos académicos pueden integrarse a través de plataformas existentes o accesibles gratuitamente.

   Los costos asociados al proyecto estarán principalmente orientados al tiempo y esfuerzo dedicados al diseño, desarrollo y pruebas de la plataforma, así como a la adquisición de licencias si fuese necesario.

   Para determinar con mayor precisión la viabilidad financiera del proyecto, los costos específicos se detallarán en el estudio de factibilidad.

7. **Licenciamiento e instalación**

El software desarrollado será de código abierto, lo que permitirá a futuros desarrolladores y académicos mejorar y personalizar la plataforma según sus necesidades. La instalación y puesta en marcha de la Plataforma de Colaboración Académica (PCAPIIS) se llevará a cabo en entornos compatibles con tecnologías web, garantizando que sea accesible desde diferentes dispositivos y navegadores.

**Requisitos de instalación**

**Para que el sistema funcione correctamente, se deben cumplir los siguientes requisitos:**

**Software necesario:**

- **Python:** Python 3.8 o superior, con las librerías necesarias como Flask, Django, Pandas, NumPy, y Matplotlib para la parte de backend y análisis de datos.
- **Base de datos:** MySQL para el almacenamiento de datos relacionados con los usuarios y actividades.
- **Entorno de desarrollo:** **Visual Studio Code** para la edición de código. Visual Studio Code es un editor de código fuente ligero, extensible y muy adecuado para trabajar con tecnologías web como HTML, CSS, JavaScript y PHP.
- **Gestión de dependencias:** pip para la instalación y gestión de librerías de Python.
- **Sistema de control de versiones:** Git para la gestión del código fuente y colaboración.

**Hardware recomendado:**

- **Procesador: Intel Core i5 o superior**
- **Memoria RAM: 8 GB o más**
- **Espacio en disco: Al menos 10 GB libres**
- **Sistema Operativo: Windows 10/11**

5. **Características del Producto**

El sistema desarrollado proporcionará una plataforma colaborativa para estudiantes, egresados y docentes de la UPT, permitiendo la gestión eficiente de información académica, interacción entre los miembros de la comunidad universitaria y la optimización de la formación académica basada en la retroalimentación y el análisis de los datos.

**Características principales:**

**Gestión de perfiles académicos:**

- Creación y administración de perfiles de estudiantes y egresados, donde podrán mostrar su trayectoria académica, proyectos, logros y habilidades.
- Integración con plataformas externas para importar información relevante como cursos completados, logros académicos y experiencias laborales previas.


**Colaboración en proyectos académicos:**

- Espacios para que los estudiantes y docentes colaboren en proyectos de investigación, prácticas profesionales y actividades extracurriculares.
- Herramientas de comunicación como foros, chats y videoconferencias para facilitar la interacción en tiempo real entre los usuarios.

**Análisis de desempeño académico:**

- Implementación de métricas y análisis de desempeño académico, donde los docentes podrán revisar la evolución de sus estudiantes.
- Generación de reportes detallados sobre el rendimiento, destacando fortalezas y áreas de mejora para cada estudiante.

**Recomendaciones personalizadas:**

- Generación de recomendaciones de cursos, actividades extracurriculares y oportunidades laborales para los estudiantes y egresados, basadas en su perfil y sus intereses académicos.
- Recomendación de ajustes en el plan curricular según las tendencias emergentes del mercado laboral y las necesidades de la industria.

**Código abierto y escalable**

- El sistema será desarrollado bajo una licencia MIT, permitiendo que futuros desarrolladores y colaboradores de la comunidad académica mejoren y adapten el sistema.
- La plataforma estará diseñada para ser escalable, permitiendo su expansión tanto en funcionalidad como en la cantidad de usuarios sin comprometer el rendimiento.

8. **Restricciones**

El desarrollo de la Plataforma de Colaboración Académica (PCAPIIS) está sujeto a algunas limitaciones técnicas y operativas, las cuales pueden afectar su funcionalidad y alcance.

**Restricciones del proyecto:**

**Restricciones en la gestión de datos académicos:**

- La plataforma depende de la disponibilidad y precisión de los datos proporcionados por los usuarios (estudiantes, egresados y docentes), lo que puede llevar a información incompleta o desactualizada si no se actualiza de manera regular.
- Los datos académicos, como las calificaciones o el historial de cursos, pueden no estar completamente estandarizados, lo que podría dificultar el análisis y la comparación entre usuarios.

**Dependencia de herramientas de terceros:**

- La plataforma se desarrollará utilizando Visual Studio Code y Python, por lo que los usuarios necesitarán contar con estos entornos para interactuar con el sistema o realizar desarrollos adicionales.

**Restricciones en la colaboración y comunicación:**

- Las funcionalidades de colaboración en tiempo real (como chats o videoconferencias) pueden depender de la estabilidad de las plataformas externas utilizadas para estos fines (Zoom, Microsoft Teams, etc.).
- La capacidad de interacción puede verse limitada por la conectividad a Internet y la disponibilidad de los servicios externos.

**Capacidad de procesamiento y rendimiento:**

- La eficiencia del sistema podría verse afectada por la cantidad de usuarios activos y la cantidad de datos procesados en tiempo real, especialmente si la plataforma no está adecuadamente escalada para manejar grandes volúmenes de información.
- La velocidad de procesamiento de grandes volúmenes de datos académicos y de interacción en tiempo real puede variar, dependiendo de la infraestructura y los recursos de hardware utilizados.





9. **Rangos de calidad**

Para garantizar que la Plataforma de Colaboración Académica (PCAPIIS) funcione de manera eficiente y ofrezca resultados confiables, se han establecido los siguientes criterios de calidad:

**Criterios de Calidad:**

**Precisión de los datos académicos:**

- El 98% de los datos académicos obtenidos (calificaciones, historial de cursos, etc.) deben ser correctos y estar completos para su uso dentro de la plataforma.
- Se implementarán mecanismos de validación para garantizar que los datos ingresados por los usuarios (estudiantes, docentes) sean consistentes y válidos.

**Eficiencia en el procesamiento y carga de datos:**

- La plataforma debe ser capaz de procesar hasta 1,000 registros de usuarios (estudiantes, docentes, egresados) por minuto sin afectar la experiencia del usuario.
- El tiempo de carga de páginas o secciones clave (como el panel de usuario o las estadísticas) no debe superar los 3 segundos en condiciones normales de uso.

**Compatibilidad y escalabilidad:**

- El sistema debe ser completamente funcional en los sistemas operativos más comunes como Windows.
- La plataforma debe permitir la incorporación de nuevas funcionalidades (como módulos de cursos adicionales, chat, foros de discusión) sin comprometer el rendimiento o la estabilidad del sistema.

**Usabilidad en la interfaz de usuario:**

- La plataforma debe contar con una interfaz intuitiva que permita a los usuarios navegar fácilmente entre las secciones (perfil académico, estadísticas, herramientas de colaboración, etc.).
- El diseño debe ser adaptable a diferentes dispositivos (PC, tabletas y teléfonos móviles) para asegurar una experiencia de usuario fluida en todos los dispositivos.

**Seguridad y privacidad de los datos:**

- Todos los datos almacenados deben cumplir con las normativas de protección de datos personales (por ejemplo, GDPR) para garantizar la privacidad y seguridad de la información de los usuarios.
- Las contraseñas y accesos deben estar cifrados, y los usuarios deben contar con métodos de autenticación seguros para acceder a sus cuentas.

10. **Precedencia y Prioridad**

- **Desarrollo de la arquitectura de la plataforma (Alta prioridad):**

  Es esencial definir la estructura general del sistema, estableciendo los módulos clave como autenticación de usuarios, foros académicos, gestión de recursos compartidos, y herramientas de interacción.

- **Registro y gestión de usuarios (Alta prioridad):**

  El sistema debe permitir la creación de perfiles para estudiantes, docentes y egresados, asegurando el acceso personalizado y seguro. Este paso es vital para habilitar las funciones de colaboración.

- **Implementación de herramientas colaborativas (Alta prioridad):**

  Se deben integrar funcionalidades como foros temáticos, mensajería interna, subida y descarga de documentos, y espacios para proyectos compartidos. Estas herramientas son el corazón del propósito de la plataforma.

- **Módulo de gestión de contenidos académicos (Media prioridad):**

  Este módulo facilitará la publicación y categorización de recursos educativos (artículos, investigaciones, presentaciones, etc.), fortaleciendo el intercambio de saberes.

- **Seguimiento y análisis de participación (Media prioridad):**

  Una vez operativa, la plataforma debe incorporar indicadores para monitorear la actividad de los usuarios, permitiendo mejorar la experiencia y evaluar el impacto académico.

11. **CONCLUSIONES**

La implementación de la Plataforma de Colaboración Académica para Proyectos Innovadores en Ingeniería de Sistemas (PCAPIIS) responde a la necesidad de fortalecer el trabajo colaborativo y la difusión de iniciativas académicas y tecnológicas dentro de la Escuela Profesional de Ingeniería de Sistemas de la UPT.

Se evidenció una carencia de espacios digitales que promuevan el intercambio activo de conocimientos, experiencias y avances en proyectos, lo cual limita el potencial de innovación, la integración entre estudiantes y docentes, y la visibilidad del talento académico.

PCAPIIS ofrece una solución accesible y escalable que fomenta la participación académica, la co-creación de contenido y la retroalimentación continua entre sus usuarios, contribuyendo directamente al desarrollo de competencias profesionales y a la mejora del aprendizaje autónomo y colaborativo.

Finalmente, la plataforma se presenta como una herramienta estratégica que puede integrarse al ecosistema académico de la UPT, permitiendo una mayor proyección de los proyectos estudiantiles, fortaleciendo la cultura de innovación y mejorando la conexión entre la universidad y su entorno profesional.

12. **RECOMENDACIONES**

- **Integrar la plataforma PCAPIIS en el plan académico** de la Escuela Profesional de Ingeniería de Sistemas, promoviendo su uso activo como herramienta de apoyo en cursos, seminarios y proyectos de investigación.
- **Fomentar la participación constante de estudiantes y docentes**, mediante incentivos académicos como reconocimiento de proyectos destacados, certificaciones internas y difusión de iniciativas exitosas dentro y fuera de la universidad.
- **Establecer una política de actualización y mantenimiento continuo** de la plataforma para asegurar su funcionalidad, adaptabilidad tecnológica y escalabilidad frente a nuevas demandas o herramientas emergentes.
- **Promover la colaboración con instituciones externas**, como empresas tecnológicas, universidades aliadas y comunidades de desarrolladores, para enriquecer los proyectos con experiencias reales del entorno profesional.
- **Implementar módulos de evaluación y retroalimentación dentro de la plataforma**, que permitan a los usuarios recibir comentarios constructivos sobre sus propuestas y facilitar la mejora continua de los proyectos académicos.
