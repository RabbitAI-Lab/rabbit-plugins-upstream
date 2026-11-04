#!/usr/bin/env python3
"""Score a small fixed flat-record contract, not arbitrary JSON or source entailment."""
import argparse,json
from pathlib import Path
FIELDS=("facility","device","status","active","count")
REQUIRED=("id","facility","device","status","active","source")

def validate(records):
    if not isinstance(records,list):raise ValueError("expected a list of records")
    seen=set()
    for row in records:
        if not isinstance(row,dict):raise ValueError("record must be an object")
        if not isinstance(row.get("id"),str) or not row["id"]:raise ValueError("nonempty string id required")
        if row["id"] in seen:raise ValueError("duplicate id: "+row["id"])
        seen.add(row["id"])
    return {r["id"]:r for r in records}

def schema_valid(row):
    if any(k not in row for k in REQUIRED):return False
    if any(not isinstance(row.get(k),str) for k in ("id","facility","device","status","source")):return False
    if type(row.get("active")) is not bool:return False
    if "count" in row and row["count"] is not None and type(row["count"]) is not int:return False
    return True

def score(gold,predicted):
    expected=validate(gold);actual=validate(predicted)
    if not all(schema_valid(r) for r in gold):raise ValueError("invalid reference schema")
    matched=set(expected)&set(actual)
    counts={"expected_records":len(expected),"predicted_records":len(actual),"matched_records":len(matched),"omitted_records":len(set(expected)-set(actual)),"unsupported_records":len(set(actual)-set(expected)),"schema_valid":all(schema_valid(r) for r in predicted),"eligible_non_null_facts":0,"correct_values":0,"grounded_correct_values":0,"wrong_values":0,"omitted_facts":0,"correct_abstentions":0,"invented_optional_values":0,"grounding_errors_on_correct_values":0}
    for identifier,reference in expected.items():
        output=actual.get(identifier)
        for field in FIELDS:
            value=reference.get(field)
            if value is None:
                if output is not None:
                    if field not in output or output[field] is None:counts["correct_abstentions"]+=1
                    else:counts["invented_optional_values"]+=1
                continue
            counts["eligible_non_null_facts"]+=1
            if output is None or field not in output or output[field] is None:
                counts["omitted_facts"]+=1;continue
            other=output[field]
            same_type=type(other) is type(value)
            equivalent=(other.casefold()==value.casefold()) if same_type and field=="status" else same_type and other==value
            if equivalent:
                counts["correct_values"]+=1
                if output.get("source")==reference["source"]:counts["grounded_correct_values"]+=1
                else:counts["grounding_errors_on_correct_values"]+=1
            else:counts["wrong_values"]+=1
    counts["record_precision"]=len(matched)/len(actual) if actual else None
    counts["record_recall"]=len(matched)/len(expected) if expected else None
    counts["value_fact_recall"]=counts["correct_values"]/counts["eligible_non_null_facts"] if counts["eligible_non_null_facts"] else None
    counts["limits"]="Fixed flat schema only. Source-pointer consistency is not semantic entailment; unsupported records scored separately. Undefined ratios are null."
    return counts

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("gold");parser.add_argument("predicted");args=parser.parse_args()
    try:result=score(json.loads(Path(args.gold).read_text()),json.loads(Path(args.predicted).read_text()))
    except (OSError,ValueError,TypeError) as exc:parser.exit(2,str(exc)+"\n")
    print(json.dumps(result,indent=2))
if __name__=="__main__":main()

