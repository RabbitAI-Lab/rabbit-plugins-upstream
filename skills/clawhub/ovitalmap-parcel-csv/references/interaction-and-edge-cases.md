# Interaction and Edge Cases

## Delivery

Send or link the actual files and label them explicitly:

```text
顶点表（导入为“标签”）：{vertices_filename}
边界表（导入为“轨迹”）：{boundary_filename}
```

Tell the user to open each CSV in 奥维地图, choose the stated import type, confirm the import page, select 导入, and confirm the import options.

## Archive model

- `{CC}_parcels.csv` is the country record.
- `master.csv` is the all-in-one cross-country record.
- New parcels update both in one locked commit.
- Archive hits are re-exported without another append.
- Corrections back up and update both records.

## Sharing the master archive

Sharing is entirely user-directed. Do not prompt automatically or prescribe email, timing, sender, recipient, or delivery service. If the user asks to share `master.csv`, follow their requested method with the available tools and never store delivery details in the archive.

## Parcel codes

Prefer a confirmed official registration/cadastre/permit ID:

```text
{CC}-{OFFICIAL_ID}
```

Otherwise use:

```text
{CC}-{YYMMDD}-{SEQ}
```

The archive allocates sequence continuity. An existing official code is blocking and requires user review; do not silently fall back to a sequential code.

## Archive hits

- Reuse the archived parcel code and provider metadata.
- Export only that parcel as its own CSV pair.
- Do not append it again.
- If a newly supplied official ID fills an empty cadastre field, update it during Step 3.
- If the user insists identical coordinates represent a different parcel, require explicit confirmation and set `allow_duplicate_coordinates: true` with a note naming the matched code.

For a mixed batch, export archive hits individually and new parcels as one batch. Present the groups separately.

## Multi-parcel batches

- Keep `parcel_ref` stable from intake through replies, CSV generation, and archive results. Numeric positions remain accepted only for backward-compatible input.
- Use one country/region per pipeline run. If parcel-level country codes differ, split the batch and preserve each parcel's ref.
- Report all current parcel-specific problems in one Chinese reply.
- If two submitted parcels have identical boundaries, request `duplicate_resolutions.{parcel_ref}`:
  - `same`: skip the later duplicate.
  - `different`: keep both, record explicit confirmation, and allow the duplicate boundary during archive commit.
- Reject duplicate non-empty official IDs before code allocation. Use `official_id_resolutions.{parcel_ref}` to correct or clear the later value.
- Never drop an unresolved parcel from run state. No CSV or archive write may occur while a batch conflict remains.

## Provider matching

- Exact normalized match: reuse automatically.
- One non-exact candidate: ask whether it is the same provider.
- Multiple top candidates: list all and ask the user to choose or create a new provider.
- No match: keep the supplied provider.
- Never merge providers based only on substring or pinyin similarity.

## Corrections

Use `archive_manager.py` action `correct` with `country_code`, `parcel_code`, and `new_vertices`. The operation must:

1. Validate the corrected polygon.
2. Require the parcel in both country and master archives.
3. Reject coordinates already belonging to another parcel.
4. Back up both archives.
5. Update both rows atomically.
6. Regenerate the corrected vertex and boundary CSV files.

Report the backup and generated file paths and ask the user to verify the new boundary.
