from pathlib import Path
import re

root = Path('.').resolve()
source_root = root.parent

unit5_src = source_root / 'Unit5'
d12 = unit5_src / 'Day12.xml'
if not d12.exists():
    d12.write_text(
        '<VSCode.Cell language="markdown">\n'
        '# Day 12: Unit 5 Assessment & Wrap-Up\n\n'
        '**Scripture Focus:** Psalm 139:14 – “I praise you because I am fearfully and wonderfully made.”\n\n'
        '**Objectives:**\n'
        '- Demonstrate understanding of Unit 5 concepts.\n'
        '- Reflect on adaptation, diversity, and stewardship.\n\n'
        '**Activities:**\n'
        '- Unit 5 Test (full 90 minutes).\n'
        '- Wrap-up discussion: “How do we see God’s wisdom in the living world?”\n'
        '</VSCode.Cell>\n',
        encoding='utf-8'
    )

out = root / 'lessons'
for unit in ['Unit4', 'Unit5']:
    src_dir = source_root / unit
    dst_dir = out / unit.lower()
    dst_dir.mkdir(parents=True, exist_ok=True)
    files = sorted(
        src_dir.glob('Day*.xml'),
        key=lambda p: int(re.search(r'Day(\d+)', p.stem).group(1))
    )
    for f in files:
        txt = f.read_text(encoding='utf-8')
        m = re.search(r'<VSCode\.Cell[^>]*>\n?(.*?)\n?</VSCode\.Cell>\s*$', txt, flags=re.S)
        body = m.group(1).strip() if m else txt.strip()
        day_num = int(re.search(r'Day(\d+)', f.stem).group(1))
        out_file = dst_dir / f'day-{day_num:02d}.md'
        out_file.write_text(body + '\n', encoding='utf-8')

index = root / 'index.md'
lines = [
    '# Dock Mennonite Biology Lesson Plans',
    '',
    'Daily one-page summaries for Unit 4 (Genetics) and Unit 5 (Evolution/Changing Environments).',
    '',
    '## Unit 4: Genetics',
]
for i in range(1, 13):
    lines.append(f'- [Day {i}](lessons/unit4/day-{i:02d}.md)')
lines += ['', '## Unit 5: Evolution and Changing Environments']
for i in range(1, 13):
    lines.append(f'- [Day {i}](lessons/unit5/day-{i:02d}.md)')
index.write_text('\n'.join(lines) + '\n', encoding='utf-8')

for unit, title, total in [
    ('unit4', 'Unit 4: Genetics', 12),
    ('unit5', 'Unit 5: Evolution and Changing Environments', 12),
]:
    p = out / unit / 'README.md'
    unit_lines = [f'# {title}', '']
    for i in range(1, total + 1):
        unit_lines.append(f'- [Day {i}](day-{i:02d}.md)')
    p.write_text('\n'.join(unit_lines) + '\n', encoding='utf-8')

readme = root / 'README.md'
readme.write_text(
    '# biology\n\n'
    'Dock Mennonite High School Biology\n\n'
    '## Lesson Plans\n'
    '- [Lesson Plan Index](index.md)\n'
    '- [Unit 4](lessons/unit4/README.md)\n'
    '- [Unit 5](lessons/unit5/README.md)\n',
    encoding='utf-8'
)

print('Created website lesson structure and index pages.')
