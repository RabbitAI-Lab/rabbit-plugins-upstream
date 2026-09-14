# Adding Suppliers

New suppliers are discovered automatically, but you can also add them manually.

## Automatic discovery

`SupplierDiscoveryEngine.run_full_discovery()` combines:
1. Seed list (58 known Iranian suppliers, `src/discovery/seed_list.py`)
2. Search engines (English + Persian queries, SerpAPI or key-less fallback)
3. B2B directory crawling via HTTrack (`_directories/` mirror store)
4. Link analysis of mirrored sites
5. Academic citation extraction
6. Iranian business registries (ISIC chemical codes)

## Manual add

```python
from src.database.models import Supplier
from src.database.session import get_db_session

db = get_db_session()
db.add(Supplier(
    company_name_en="Example Chem Co.",
    company_name_fa="شرکت شیمی نمونه",
    website_url="https://example-chem.ir",
    supplier_type="distributor",
    city="Tehran", country="IR",
    crawl_frequency_hrs=24,
))
db.commit()
```

## Verify a URL

```python
from src.discovery.validator import SupplierValidator
score = SupplierValidator().score("https://example-chem.ir")  # 0-100
```

Scores ≥ 60 (config: `discovery.min_verification_score`) are accepted.

## Per-supplier HTTrack overrides

In `config.yaml`:

```yaml
httrack:
  supplier_overrides:
    "example_chem_co":
      connections_per_second: 0.5
      sockets: 1
      max_rate: 10000
```

## Legal

Only mirror sites you are authorized to archive. Respect robots.txt and each
site's terms of service. Collected data is a research/procurement reference;
verify every supplier before relying on it.
