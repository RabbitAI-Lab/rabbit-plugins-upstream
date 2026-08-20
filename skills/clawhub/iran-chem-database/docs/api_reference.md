# API Reference

Base URL: `http://localhost:8000/api/v1/`

| Method | Path | Description |
|---|---|---|
| GET | `/molecules` | Search/list molecules (paginated) |
| GET | `/molecules/{inchi_key}` | Molecule detail |
| GET | `/molecules/search?q=&cas=&smiles=&formula=` | Full-text / CAS / SMILES / formula search |
| GET | `/suppliers` | List suppliers |
| GET | `/suppliers/{id}` | Supplier detail |
| GET | `/suppliers/{id}/mirror-status` | HTTrack mirror health/status |
| GET | `/mirrors` | All HTTrack mirror statuses |
| GET | `/mirrors/{id}/changes` | Recent changes from hts-changes.json |
| GET | `/stats` | Global database statistics |
| GET | `/updates/recent` | Recently added/changed molecules |
| GET | `/export?format=csv\|json\|sdf` | Export database |
| GET | `/health` | Service health |
| GET | `/crawl-logs` | Recent crawl history |

## Example queries

```bash
curl "http://localhost:8000/api/v1/molecules/search?q=ethanol"
curl "http://localhost:8000/api/v1/molecules/search?cas=64-17-5"
curl "http://localhost:8000/api/v1/molecules/search?formula=C2H6O"
curl "http://localhost:8000/api/v1/molecules/search?q=اتانول"
curl "http://localhost:8000/api/v1/export?format=csv"
```

Query parameters for `/molecules`:
`query`, `cas`, `formula`, `grade`, `supplierId`, `minPurity`, `available`,
`page`, `limit`.
