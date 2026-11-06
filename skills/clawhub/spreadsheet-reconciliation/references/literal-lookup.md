# Literal-key lookup: tested pattern

This reporting pattern assumes case-sensitive text identifiers. Leading zeros, spaces, *, ?, ~ and comparison characters are literal. Source columns remain unchanged. If the source defines different identity rules, normalize in separate columns and use the same rule for both counting and retrieval.

## Layout

Roster A2:A20 contains text IDs, B2:B20 names and C2:C20 values. Lookup A2 contains the requested ID. The bounded ranges must cover the full roster; extend all aligned ranges together when adding rows. Do not replace them with costly whole-column array scans.

In Roster D2, classify the original value before retrieval and fill through D20:

```gs
=ISLOGICAL(C2)
```

In Lookup I2, count literal identity matches:

```gs
=IF(A2="",0,SUMPRODUCT(--EXACT(A2,Roster!$A$2:$A$20)))
```

In Lookup E2, return the name only when one identity matches:

```gs
=ARRAYFORMULA(IF(A2="","MISSING KEY",IF(I2=0,"UNMATCHED",IF(I2>1,"MULTIPLE",XLOOKUP(TRUE,EXACT(A2,Roster!$A$2:$A$20),IF(LEN(Roster!$B$2:$B$20)=0,"MISSING VALUE",Roster!$B$2:$B$20),"UNMATCHED",0)))))
```

In Lookup J2, return the value with explicit missing and boolean reporting states:

```gs
=ARRAYFORMULA(IF(A2="","MISSING KEY",IF(I2=0,"UNMATCHED",IF(I2>1,"MULTIPLE",IF(XLOOKUP(TRUE,EXACT(A2,Roster!$A$2:$A$20),Roster!$D$2:$D$20,FALSE,0),IF(XLOOKUP(TRUE,EXACT(A2,Roster!$A$2:$A$20),Roster!$C$2:$C$20,FALSE,0),"BOOLEAN TRUE","BOOLEAN FALSE"),XLOOKUP(TRUE,EXACT(A2,Roster!$A$2:$A$20),IF(LEN(Roster!$C$2:$C$20)=0,"MISSING VALUE",Roster!$C$2:$C$20),"UNMATCHED",0))))))
```

The ARRAYFORMULA wrapper is required in the Google Sheets lookup expressions shown here: it makes the EXACT predicate and transformed return values full arrays. Without it, XLOOKUP can receive a scalar predicate and report mismatched array sizes. Fill the Lookup formulas down for actual input rows. Both counting and retrieval use EXACT. An empty input is MISSING KEY; no match is UNMATCHED; conflicting duplicates are MULTIPLE. No duplicate gets a first-record value as an authoritative answer.

## Value meanings

A known numeric 0 remains a number. A truly empty source and a source formula returning an empty string produce MISSING VALUE. This marker is text, not a physically empty output cell. A source boolean produces BOOLEAN FALSE or BOOLEAN TRUE text in the report; it is not coerced to numeric 0/1. Raw source booleans remain intact.

The source-side ISLOGICAL helper is deliberate: determine source type before lookup/array coercion. If a numeric-only contract rejects boolean input, flag that type violation instead of treating it as a measured zero.

These mixed reporting columns are for inspection. For a structured dataset, keep the match/value status and typed value as separate fields under the output schema; do not silently parse markers as measurements. SUM and COUNT ignore the text markers, but missingness and ambiguity need separate explicit counts. A reserved marker that could also occur as a legitimate source value requires a separate status field.

A first-match fallback can use ARRAYFORMULA(INDEX(...,MATCH(TRUE,EXACT(...),0))) after the uniqueness guard. Preserve the explicit array context in Google Sheets. Do not use raw pattern-capable identifier matching as a substitute.

## Verification scope

The shown form was executed in native Google Sheets with locale en_US. The same formula bodies without the outer ARRAYFORMULA wrapper passed the scoped LibreOffice 26.2.5.2 regression. Both runs retain actual values and source-preservation evidence outside the skill. Excel has not been executed. Do not infer compatibility with older versions or all locales from these checks.
