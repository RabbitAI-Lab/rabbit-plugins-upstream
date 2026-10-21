"""Render a completed packet with the original pure DOCX producers. No API calls."""
import argparse,hashlib,json,os,tempfile
from pathlib import Path
from resume_layout import build, validate_blocks
from letter_layout import make_letter, validate_letter

def render(packet,destination,resume=False):
 out=Path(destination)
 lines=packet['cover_letter_lines'];contacts=packet.get('contact_lines_count')
 validate_letter(lines,contacts)
 validate_blocks(packet['resume_blocks'])
 if packet.get('letter_spacing','standard') not in ['standard','compact']:
  raise ValueError('letter_spacing must be standard or compact')
 packet_text=json.dumps(packet,indent=2,ensure_ascii=False)+'\n'
 packet_file=out/'packet.json'
 if not resume and any((out/name).exists() for name in ['Resume.docx','Resume.layout.json','Letter.docx','Letter.layout.json','packet.json']):
  raise ValueError('Preserve existing files; choose a new revision directory')
 if resume and (not packet_file.is_file() or json.loads(packet_file.read_text(encoding='utf-8'))!=packet):
  raise ValueError('Resume requires the same saved packet; choose a new revision directory for changed wording or layout')
 letter_path=out/'Letter.docx';letter_receipt_path=out/'Letter.layout.json'
 if letter_path.exists():
  if not letter_receipt_path.is_file():raise ValueError('Existing letter has no receipt; preserve it and choose a new revision directory')
  letter_receipt=json.loads(letter_receipt_path.read_text(encoding='utf-8'))
  if (letter_receipt.get('source_lines')!=lines or letter_receipt.get('contact_lines_count')!=contacts
      or letter_receipt.get('letter_spacing')!=packet.get('letter_spacing','standard')
      or letter_receipt.get('docx_sha256')!=hashlib.sha256(letter_path.read_bytes()).hexdigest()):
   raise ValueError('Existing letter differs from its saved receipt; preserve it and choose a new revision directory')
 elif letter_receipt_path.exists():
  raise ValueError('An existing letter receipt needs a separate revision directory')
 out.mkdir(parents=True,exist_ok=True)
 if not resume:
  with packet_file.open('x',encoding='utf-8') as f:f.write(packet_text)
 # Build each file off to the side; publish complete files without overwriting.
 with tempfile.TemporaryDirectory(prefix='.jobgenie-build-',dir=out) as temporary:
  staging=Path(temporary)
  if (out/'Resume.docx').exists():
   receipt_path=out/'Resume.layout.json'
   if not receipt_path.is_file():raise ValueError('Existing resume has no receipt; preserve it and choose a new revision directory')
   receipt=json.loads(receipt_path.read_text(encoding='utf-8'))
   if receipt.get('source_blocks')!=packet['resume_blocks'] or receipt.get('docx_sha256')!=hashlib.sha256((out/'Resume.docx').read_bytes()).hexdigest():
    raise ValueError('Existing resume differs from its saved receipt; preserve it and choose a new revision directory')
  else:
   if (out/'Resume.layout.json').exists():raise ValueError('An existing resume receipt needs a separate revision directory')
   receipt=build({'blocks':packet['resume_blocks']},staging/'Resume.docx')
   os.link(staging/'Resume.docx',out/'Resume.docx')
   os.link(staging/'Resume.layout.json',out/'Resume.layout.json')
  if not (out/'Letter.docx').exists():
   make_letter(lines,staging/'Letter.docx',contact_lines=contacts,spacing=packet.get('letter_spacing','standard'))
   letter_receipt={'source_lines':lines,'contact_lines_count':contacts,
                   'letter_spacing':packet.get('letter_spacing','standard'),
                   'docx_sha256':hashlib.sha256((staging/'Letter.docx').read_bytes()).hexdigest()}
   (staging/'Letter.layout.json').write_text(json.dumps(letter_receipt,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
   os.link(staging/'Letter.docx',out/'Letter.docx')
   os.link(staging/'Letter.layout.json',out/'Letter.layout.json')
 return receipt

if __name__=='__main__':
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('packet');p.add_argument('destination');p.add_argument('--resume',action='store_true',help='Complete missing files for the identical saved packet; preserve existing documents');a=p.parse_args()
 render(json.loads(Path(a.packet).read_text(encoding='utf-8')),a.destination,resume=a.resume)
 print('Built Resume.docx and Letter.docx. Export/inspect requested pages before calling delivery complete.')
