---
name: mc-mod-translate
description: Translate Minecraft Java Edition mod content from English to Chinese using a community-maintained dictionary (Dict-Sqlite.db, 900K+ entries from i18n-Dict-Extender) and zh.minecraft.wiki for vanilla game terms. Use when translating mod language files (.lang/.json), FTB Quests SNBT files, config files, Patchouli books, or any text content in Minecraft mods. Prioritizes dictionary matches, falls back to wiki lookup, then context-based agent translation.
version: 2.1.0
---

# Minecraft Mod Translation

Translate Minecraft Java Edition mod content from English to Simplified Chinese, using a community-maintained dictionary of 900K+ entries covering vanilla items and 3,500+ mods, plus zh.minecraft.wiki for vanilla term lookup.

## Prerequisites

### Dictionary database

The translation dictionary is a pre-built SQLite database (`Dict-Sqlite.db`) auto-updated weekly by the [i18n-Dict-Extender](https://github.com/VM-Chinese-translate-group/i18n-Dict-Extender) project. It merges CFPA community translations with directly-maintained mod translations.

**Download the latest dictionary** (run once, or when updates are needed):

```bash
python3 scripts/fetch_dict.py
```

This downloads `Dict-Sqlite.db` (~142 MB) from the latest GitHub release. Use `--force` to re-download, or `--check` to see if an update is available.

The DB schema:
```sql
CREATE TABLE dict(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    ORIGIN_NAME TEXT NOT NULL,  -- English original
    TRANS_NAME  TEXT NOT NULL,  -- Chinese translation
    MODID       TEXT NOT NULL,  -- Mod ID (e.g. minecraft, tconstruct)
    KEY         TEXT NOT NULL,  -- Lang key (e.g. block.minecraft.stone)
    VERSION     TEXT NOT NULL,  -- Game version
    CURSEFORGE  TEXT NOT NULL   -- CurseForge slug
);
```

### Vanilla term lookup

Vanilla Minecraft terms are looked up via [zh.minecraft.wiki](https://zh.minecraft.wiki/) MediaWiki API. The wiki has English-named pages that redirect to Chinese-named pages (e.g., "Copper Ingot" redirects to "铜锭"), providing authoritative translations for vanilla game content. No local files needed — lookups are performed on-demand by `query.py`.

## Translation Workflow

### Step 1: Download / update the dictionary (if needed)

```bash
# Check if update is available
python3 scripts/fetch_dict.py --check

# Download (skips if already up-to-date)
python3 scripts/fetch_dict.py
```

### Step 2: Identify the mod

Determine the `modid` from context:

- **File path**: `assets/<modid>/lang/`, `config/<modid>/`, `<modid>/quests/`
- **Lang keys**: `block.<modid>.xxx`, `item.<modid>.xxx`, `entity.<modid>.xxx`
- **Mod metadata**: `META-INF/mods.toml`, `mcmod.info`, `fabric.mod.json`
- **File name**: quest files often contain the mod name

If the modid is unknown, search for it:

```bash
python3 scripts/query.py --list-mods --search <keyword>
```

### Step 3: Query the dictionary

Pull all known translations for the mod to use as a glossary:

```bash
python3 scripts/query.py --modid <modid> --limit 10000
```

This outputs TSV: `origin_name \t trans_name \t modid \t key \t source`.

For looking up individual terms during translation:

```bash
# By English text (dict + wiki fallback)
python3 scripts/query.py --text "Copper Ingot"

# Dict only, skip wiki
python3 scripts/query.py --text "Copper Ingot" --no-wiki

# By lang key
python3 scripts/query.py --key "block.tconstruct.copper_block"
```

The `--text` query searches the dictionary first, then falls back to zh.minecraft.wiki for vanilla MC terms via redirect resolution.

### Step 4: Translate

Apply these rules in priority order:

1. **Dictionary match (highest priority)**: If the English text or lang key exists in Dict-Sqlite.db, use the `TRANS_NAME` exactly.
2. **Wiki lookup**: If no dict match, query.py falls back to zh.minecraft.wiki — if the English name redirects to a Chinese page, that page title is the translation.
3. **Context-based translation**: If neither source has a match, translate based on Minecraft domain knowledge and surrounding context. Keep terminology consistent with existing dictionary entries for the same mod.

## File Type Handling

### Language files (.lang / .json)

**1.12.2 and earlier** — `.lang` files, `key=value` format:
```
item.example_mod.copper_ingot=Copper Ingot
```
Translate only the value (right side of `=`). Never modify the key.

**1.13+** — `.json` files, key-value JSON:
```json
{
  "item.example_mod.copper_ingot": "Copper Ingot",
  "block.example_mod.copper_block": "Copper Block"
}
```
Translate only the string values. Preserve JSON structure and escaping.

### FTB Quests SNBT files

SNBT format with unquoted keys and tab indentation. Only translate these fields:

- `title:` — quest title
- `subtitle:` — quest subtitle (single quoted string)
- `description:` — array of quoted strings

Rules:
- Skip quests whose `title:` starts with `Any` (auto-generated, not for translation)
- Preserve `{image:...}` tags, URLs, color codes (`&6`, `&r`, etc.), and `''bold''` markup
- Keep the SNBT structure intact — do not change keys, arrays, or indentation
- Preserve quest dependency references and icon names

Example:
```
title: A Copper Age
subtitle: "Smelt your first copper ingot"
description: ["Welcome to the copper age! {image:gold_ingot.png}"]
```
Translate to:
```
title: 铜器时代
subtitle: "冶炼你的第一块铜锭"
description: ["欢迎来到铜器时代！ {image:gold_ingot.png}"]
```

### Config files

Translate only human-readable description strings in config files. Do not modify keys, paths, or numeric values.

### Patchouli books

Translate text content in JSON book files. Preserve macro commands (`$(...)`) and page references.

## Translation Conventions

Maintain consistency with Minecraft community conventions:

- Block/item names: use standard MC Chinese terms (e.g., "Ingot" → "锭", "Block" → "方块", "Ore" → "矿石")
- Biome names: end with appropriate suffix (e.g., "Plains" → "平原", "Forest" → "森林")
- Entity names: match vanilla entity translations
- Enchantment names: use standard enchantment translations
- Potion effect names: use standard effect translations
- Tool/material names: "Sword" → "剑", "Pickaxe" → "镐", "Axe" → "斧", "Shovel" → "锹", "Hoe" → "锄"

When translating for a specific mod, prefer that mod's existing dictionary translations for consistency.

## Output

Save translated files to the designated output directory. Preserve the original file structure and encoding. For `.lang` files use UTF-8 (without BOM). For `.json` files ensure valid JSON. For SNBT files preserve tab indentation and unquoted key style.

## Verification

After translation, verify:

1. No English text remains in translated fields (except preserved tags, URLs, commands)
2. File structure is intact (valid JSON/SNBT/lang format)
3. Dictionary translations were applied where matches existed
4. Terminology is consistent across all entries in the same file
