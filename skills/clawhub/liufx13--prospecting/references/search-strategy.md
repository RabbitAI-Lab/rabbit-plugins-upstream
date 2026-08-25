# Search Strategy Framework

## Core Principles

| Principle | Description |
|-----------|-------------|
| **Multi-center** | Large cities: 3-6 search centers to avoid missing suburbs |
| **Keyword matrix** | 4-6 keyword combinations per center |
| **Pagination** | Scroll and load 3 times per search |
| **Deduplication** | Cross-center, cross-keyword deduplication |
| **Data integrity** | All data must come from real sources, no fabrication |
| **Self-optimization** | Auto-detect gaps, adjust keywords, expand coverage |

---

## 0. Self-Optimization Protocol (NEW)

### 0.1 Coverage Targets by Market Size

| City Population | Minimum Centers | Target Prospects | Auto-Expand If Below |
|-----------------|-------------------|------------------|----------------------|
| < 500k | 1-2 | 15-25 | 10 |
| 500k - 2M | 3-4 | 30-50 | 25 |
| > 2M | 6-8 | 60-80 | 50 |
| > 5M (metro) | 8-12 | 80-120 | 60 |

**Houston example**: 7M metro → 11 centers → 90 prospects (meets target)

### 0.2 Auto-Expansion Triggers

After Pass 1 (core keywords), if unique prospects < target:

| Trigger | Threshold | Action |
|---------|-----------|--------|
| Low yield | <50% of target after Pass 1 | Add satellite centers |
| Geographic gaps | >15mi between centers | Add midpoint center |
| Chain under-rep | Known chains missing | Add brand searches |
| Suburban blindspot | Downtown-heavy results | Add outer ring centers |

### 0.3 Satellite Center Selection

When expanding, pick centers based on:
1. **Population density** (Google Maps visible density)
2. **Known commercial zones** (industrial parks, auto rows)
3. **Midpoint between existing centers** (fill gaps)
4. **Satellite cities** (independent municipalities in metro)

**Houston expansion example**:
- Initial: Downtown, Katy, Sugar Land, The Woodlands, Baytown, Cypress (6 centers)
- Expanded: +Pearland, Pasadena, Galveston, Spring, Humble (11 centers)
- Reason: Initial 6 centers yielded 50 prospects (<60 target for 7M metro)

---

## 1. Center Point Selection

| City Size | Centers | Radius | Examples |
|-----------|---------|--------|----------|
| < 500k | 1 (downtown) | 30mi | Small cities |
| 500k-2M | 2-3 | 20mi | Austin, Seattle |
| > 2M | 4-6 | 15mi | Houston, Dallas, LA |
| > 5M metro | 8-12 | 10-15mi | Houston metro, Dallas-Fort Worth |

### Houston Example (6 → 11 centers)
**Initial 6**:
- Downtown (core)
- Katy (west)
- Sugar Land (southwest)
- The Woodlands (north)
- Baytown (east industrial)
- Cypress (northwest)

**Expanded +5**:
- Pearland (south)
- Pasadena (southeast industrial)
- Galveston (coast, tourism+local)
- Spring (north suburban)
- Humble (northeast, FM 1960 corridor)

### Dallas-Fort Worth Example (12 centers)
- Downtown Dallas
- Plano (north)
- Fort Worth (west)
- Arlington (south)
- Frisco (northeast)
- Irving (mid-cities)
- Garland (east)
- Denton (northwest)
- McKinney (northeast)
- Mesquite (east)
- Grand Prairie (southwest)
- Carrollton (north central)

---

## 2. Keyword Matrix

### 2.1 Structure

| Type | Purpose | Examples |
|------|---------|----------|
| **Core** | Industry standard | auto body shop, collision repair |
| **Service** | Sub-services | paint shop, body work, refinishing |
| **Equipment** | Equipment needs | spray booth, frame machine, car lift |
| **Brand** | Chain brands | Caliber, CARSTAR, Maaco, Crash Champions |
| **Scene** | Customer type | fleet repair, commercial vehicle, dealer |

### 2.2 By Industry

**Auto Body / Collision**
```
auto body shop
auto body repair
collision repair
collision center
paint shop
auto paint shop
```

**Manufacturing / CNC**
```
machine shop
CNC machining
metal fabrication
fabrication shop
precision machining
```

**HVAC**
```
HVAC contractor
heating and cooling
air conditioning service
commercial HVAC
```

---

## 3. Pagination Protocol

```
Search keyword → wait 5s → extract first 8
    ↓
Scroll → wait 3s → extract new 5-8
    ↓
Scroll → wait 3s → extract new 5-8
    ↓
Scroll → wait 3s → extract any remaining
    ↓
Done
```

**Key**: Wait 2-3s after each scroll for Google Maps to load.

---

## 4. Deduplication Rules

| Case | Criteria | Action |
|------|----------|--------|
| Exact duplicate | Same name + address | Keep more complete |
| Chain multi-location | Same name + different address | Keep (mark as chain) |
| Address reuse | Same address + different name | Keep (may be different business) |
| Closed | Maps shows "permanently closed" | Remove |
| Wrong industry | e.g. pure car wash | Remove |

---

## 5. Data Integrity Markers

### Markers

| Marker | Meaning | Use When |
|--------|---------|----------|
| `verified` | Verified real | Phone/address from Google Maps |
| `restricted_view` | Limited view | Review count, website URL not available |
| `unverified` | Not verified | Needs confirmation |
| `placeholder` | Placeholder | **DO NOT use for calling** |

### Field Annotation Example

```json
{
  "phone": "(713) 668-3639",
  "phone_status": "verified",
  "rating": "4.8",
  "rating_source": "visible_in_feed",
  "reviews_count": null,
  "reviews_count_note": "restricted_view",
  "raw_notes": "Google Maps restricted view. Phone and rating visible. Reviews count hidden."
}
```

---

## 6. Execution Checklist

```
□ Step 1: Determine city size → select center count + target prospects
□ Step 2: Determine industry → select keyword matrix (4-6 keywords)
□ Step 3: Pass 1 - Core search
    □ Center 1: Keyword 1-6 → paginate 3x → extract
    □ Center 2: Keyword 1-6 → paginate 3x → extract
    □ ... all initial centers
□ Step 4: Auto-analyze Pass 1
    □ Count unique prospects
    □ Check vs target (15/30/60/80)
    □ Identify zero-result combos
    □ Identify missing chains
□ Step 5: Pass 2 - Gap-fill (if needed)
    □ Swap low-yield keywords
    □ Add missing brand searches
    □ Add satellite centers if below target
□ Step 6: Pass 3 - Equipment/Brand deep dive
    □ Equipment keywords
    □ Explicit brand+city searches
□ Step 7: Deduplicate
    □ Same name+address: keep one
    □ Mark chain brands
    □ Remove closed/non-target
□ Step 8: Validate
    □ Mark field sources
    □ Mark restricted fields
    □ Check for placeholder phones
□ Step 9: Score and tier
    □ Chain/large (🔴 high)
    □ Mid independent (🟡 medium)
    □ Small independent (🟢 low)
□ Step 10: Generate output
    □ index.json
    □ P###.json
    □ call-list.csv
    □ coverage-report.json
□ Step 11: Archive
    □ candidates-raw.txt
    □ Note search time, keywords, centers, auto-adjustments
```

---

## 7. Prohibitions (Enforced)

| Prohibition | Rule |
|-------------|------|
| ❌ Fake phones | No (XXX) 555-XXXX format |
| ❌ Fake addresses | Must come from Maps extraction |
| ❌ Fake ratings | Must be visible in Maps |
| ❌ Fake review counts | Must be from Maps or marked restricted |
| ❌ Fake websites | Must be extracted or marked unavailable |

---

## 8. Cross-City / Cross-Industry

### Cities

| City | Centers | Expanded |
|------|---------|----------|
| Dallas | Downtown, Plano, Fort Worth, Arlington, Frisco | +Irving, Garland, Denton, McKinney, Mesquite, Grand Prairie, Carrollton |
| Austin | Downtown, Round Rock, Cedar Park, South Austin | +Pflugerville, Leander, Georgetown, Buda, Kyle |
| Miami | Downtown, Fort Lauderdale, West Palm Beach | +Hialeah, Miami Beach, Coral Gables, Doral, Kendall |
| Houston | Downtown, Katy, Sugar Land, The Woodlands, Baytown, Cypress | +Pearland, Pasadena, Galveston, Spring, Humble |

### Industries

| Industry | Core Keywords | Service Keywords | Equipment Keywords |
|----------|-------------|------------------|-------------------|
| Auto Body | auto body shop, collision repair | paint shop, body work | spray booth, frame machine |
| Manufacturing | machine shop, CNC machining | metal fabrication, welding | CNC mill, lathe |
| HVAC | HVAC contractor, heating cooling | air conditioning, furnace | commercial HVAC |
| Dental | dental lab, dental clinic | orthodontic, prosthodontic | CAD/CAM, 3D printing |

---

## 9. FAQ

**Q: Google Maps restricted view?**
A: Mark restricted status. Try: login to Maps, visit website, use Yelp/Yellow Pages.

**Q: Too few results?**
A: Check: center too remote? keywords too narrow? enough pagination? expand radius?

**Q: Chain brands?**
A: Keep all locations (different address = different customer). Mark as chain. Priority contact.

**Q: When to stop expanding?**
A: Stop when: (a) prospect count meets target for city size, OR (b) marginal gain <5 prospects per new center, OR (c) all known satellite cities covered.

---

## File Naming

```
prospect-data/
├── {city}-{state}-{date}/
│   ├── profile-{customer-name}.json
│   ├── candidates-raw.txt
│   ├── candidates.json
│   ├── index.json
│   ├── coverage-report.json
│   ├── P001.json ~ P0XX.json
│   └── call-list.csv
```

---

## Version

- **Version**: 2.0.0
- **Date**: 2026-05-23
- **Changes**: Added self-optimization protocol, auto-expansion triggers, satellite center selection, coverage targets by market size
- **Scope**: All B2B proactive prospecting projects
