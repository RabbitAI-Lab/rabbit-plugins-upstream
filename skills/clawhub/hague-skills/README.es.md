🌐 [中文](README.md) · [繁體中文](README.zh-Hant.md) · [English](README.en.md) · [Français](README.fr.md) · **Español** · [العربية](README.ar.md) · [日本語](README.ja.md) · [Русский](README.ru.md)

<p align="center"><img src="logo.png" alt="Hui Ning IP" width="150"></p>

# Hague Design System · Competencia práctica para el registro internacional de diseños industriales

> *«Una sola pregunta, una respuesta lista para el expediente en el sistema de La Haya.»*
> *"Ask once. Get a filing-ready Hague design practice answer."*

[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Version](https://img.shields.io/badge/version-1.10.8-blue.svg)](references/changelog.md)
![Agent-Agnostic](https://img.shields.io/badge/Agent-Agnostic-blueviolet)
[![Hague Members](https://img.shields.io/badge/Hague%20Members-83-green)](https://www.wipo.int/en/web/hague-system)
![No-Fabrication](https://img.shields.io/badge/Principle-No--Fabrication-orange)

**Una competencia integral del sistema de La Haya para agentes de diseños, abogados de PI y departamentos legales de todo el mundo — centrada en la fase internacional de la OMPI, utilizable desde la perspectiva de cualquier parte contratante, con un capítulo opcional sobre la OMPIC/China.**

No es una enciclopedia: ofrece rutas de verificación para cada hito de presentación y examen, fuentes jurídicas verificables cláusula por cláusula (Acta de Ginebra / Reglamento Común / Instrucciones Administrativas / Guía), especificaciones numéricas para las reproducciones, la unidad de diseño y la prioridad, y parámetros de tasas y plazos revisables (con un script integrado de cálculo de tasas).

Basada en el formato universal Agent Skills (`/SKILL.md`); funciona con cualquier agente compatible con skills.

[Qué hace](#qué-hace) · [Instalación](#instalación) · [Mecanismos clave](#mecanismos-clave) · [Estructura del repositorio](#estructura-del-repositorio) · [Alcance y límites](#alcance-y-límites)

---

## Instalación

### Opción 1: script de sincronización (recomendado)

```bash
# Windows
py -3 scripts/sync_to_local.py

# macOS / Linux
python3 scripts/sync_to_local.py

# Opciones habituales
py -3 scripts/sync_to_local.py --dry-run                # previsualización, sin escritura
py -3 scripts/sync_to_local.py --target D:/path/to/skills   # directorio de skills personalizado
```

El script sincroniza, en un solo sentido, este repositorio como una única skill con su directorio local de skills (por defecto `~/.workbuddy/skills`, instalada como `hague-design-system/`): los archivos nuevos o modificados se sobrescriben, los obsoletos se eliminan y **los metadatos locales como `_user_meta.json` se conservan**; los archivos propios del repositorio (README, LICENSE, logo, etc.) nunca se instalan en el directorio de skills.

### Opción 2: copia manual

Copie la carpeta completa del repositorio en su directorio de skills (p. ej. `~/.workbuddy/skills/`) y cámbiele el nombre a `hague-design-system`; después reinicie o recargue la aplicación.

> ⚠️ Es una skill de varios archivos: la base de conocimiento de `references/` (Acta y Reglamento Común, Instrucciones Administrativas, Guía del sistema de La Haya, capítulo opcional sobre China, etc.) se referencia desde `SKILL.md` mediante rutas relativas `@` — **un solo archivo ausente rompe la cadena**. Copie directorios completos; no tome solo `SKILL.md`.

## Qué hace

| Área | Descripción |
|------|------|
| Solicitud internacional | Derecho a presentar; presentación DM/1 y eHague; requisitos de las reproducciones; unidad de diseño; prioridad; vías de presentación e hitos del procedimiento |
| Registro y publicación | Examen formal y correcciones; registro internacional y fecha de registro; publicación y aplazamiento; retiradas |
| Examen y recursos | Respuesta a las denegaciones de las Oficinas designadas; declaraciones de concesión de protección y sus efectos; nulidad; vías tras la denegación |
| Renovación y cambios | Duración y renovación (incluido el plazo de gracia); cambio de titular, de datos del titular, de representante, limitación, renuncia |
| Tasas | Los siete tipos de operaciones de tasas (solicitud / renovación / cambio de titular / cambio de datos del titular / cambio de nombre y dirección del creador / limitación / renuncia); calculadora de tasas de La Haya; estructura de tasas en CHF; script integrado de cálculo |
| Búsqueda | Búsqueda de antecedentes y situación jurídica en DesignDB |
| Opcional · Capítulo China | Declaraciones de China; examen y recursos ante la OMPIC; transmisión y operaciones del sistema; solicitudes divisionales; notas en CNY (los profesionales fuera de China pueden omitirlo por completo) |

## Mecanismos clave

1. **Núcleo universal**: la fase internacional de la OMPI (común a todas las partes contratantes) es el cuerpo principal; el capítulo OMPIC/China es opcional y los profesionales fuera de China pueden omitirlo por completo;
2. **Fuente jurídica y de datos única**: los datos volátiles (tasas, declaraciones) convergen en una única fuente autorizada; el historial de versiones y el índice de archivos se centralizan (`changelog.md`, `11-file-index.md`) para evitar divergencias;
3. **Divulgación progresiva**: los textos extensos (incluida la Guía del sistema de La Haya, 286 KB) residen en `references/`, se cargan a demanda y disponen de índice por número de línea, sin saturar el contexto;
4. **«Ninguno» cuando no hay fuente**: la información dudosa se señala de inmediato — sin disposiciones, plazos ni importes inventados; las respuestas entregadas nunca usan tablas Markdown (listas y definiciones en línea en su lugar).

## Estructura del repositorio

```text
HAGUE-SKILLS/                        # Raíz del repositorio = raíz de la skill (repositorio de una skill)
├── SKILL.md                         # Plano de control: rol / tarea / contexto / proceso / reglas / salida
├── references/                      # 12 archivos de conocimiento (incl. capítulo China opcional, changelog, índice)
├── scripts/                         # Scripts de la skill (calculadora, asistente) + sync_to_local.py
├── README.md                        # 简体中文 (predeterminado)
├── README.zh-Hant.md                # 繁體中文
├── README.en.md                     # English
├── README.fr.md                     # Français
├── README.es.md                     # Español (este archivo)
├── README.ar.md                     # العربية (RTL)
├── README.ja.md                     # 日本語
├── README.ru.md                     # Русский
├── LICENSE                          # Licencia MIT
└── logo.png                         # Marca (encabezado del README)
```

- La raíz del repositorio es la raíz de la skill; una vez instalada, la estructura es estrictamente de **2 niveles** (`SKILL.md` / `references/` / `scripts/`), conforme a la estructura oficial de WorkBuddy;
- Los archivos propios del repositorio (`README*.md`, `LICENSE`, `logo.png`, `scripts/sync_to_local.py`) nunca se instalan en el directorio de skills;
- Archivos de skill: **CRLF, UTF-8 sin BOM**.

## Datos y vigencia

- Las fuentes jurídicas siguen las **versiones oficiales vigentes de la OMPI / la OMPIC**; la skill indica la fecha de referencia de los datos y el ciclo de revisión recomendado (lista §3.0);
- Para datos volátiles (tasas, tasas de designación individual, declaraciones, tipos de cambio), vuelva a verificar las últimas publicaciones oficiales o la calculadora de tasas antes de usarlos en un expediente;
- La salida es una referencia práctica — **no constituye asesoramiento jurídico**.

## Alcance y límites

- No sustituye el criterio oficial ni el del caso concreto: los plazos, las tasas y las conclusiones procedimentales se rigen por las notificaciones de la Oficina designada y las publicaciones oficiales;
- Sin invención: los datos que no pueden encontrarse se responden como «ninguno»;
- La cobertura jurídica se centra en el procedimiento y las reglas comunes del sistema de La Haya; el derecho sustantivo y la práctica de examen de cada parte contratante designada siguen las posiciones oficiales de esa parte.

## License

[MIT](LICENSE) © 2026 Hui Ning IP（辉宁知识产权）.

- El contenido de la propia skill (organización y anotaciones en `SKILL.md` y `references/`) está bajo MIT;
- Los textos oficiales de la OMPI reproducidos o citados en `references/` (Acta de Ginebra, Reglamento Común, Instrucciones Administrativas, Guía, etc.) siguen siendo propiedad de la OMPI y no están cubiertos por esta licencia.

## Contacto

- Preguntas y sugerencias: abra un Issue en este repositorio;
- Creada y mantenida por Hui Ning IP (un equipo chino de agentes de patentes).
