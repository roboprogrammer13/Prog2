"""
Jednoduchý skript pro vykreslení grafů (výšky hor).

Behavior:
 - Pokud je dostupný matplotlib, použije ho a uloží PNG obrázky.
 - Pokud matplotlib není nainstalovaný, vygeneruje samostatný HTML soubor s vestavěnými SVG grafy
   (žádné další knihovny není třeba instalovat) a otevře ho ve výchozím prohlížeči.

Spuštění: dvojklikem nebo v Powershellu:
	python .\bigData.py

"""

import os
import sys
import math
import webbrowser
from operator import itemgetter
from pathlib import Path

try:
	import matplotlib.pyplot as plt
	HAS_MATPLOTLIB = True
except Exception:
	HAS_MATPLOTLIB = False


def get_sample_data():
	"""Vrátí seznam (jméno, výška[m])"""
	return [
		("Mount Everest", 8848),
		("K2", 8611),
		("Kangchenjunga", 8586),
		("Lhotse", 8516),
		("Makalu", 8485),
		("Cho Oyu", 8188),
		("Dhaulagiri", 8167),
		("Manaslu", 8163),
		("Nanga Parbat", 8126),
		("Annapurna", 8091),
	]


def plot_with_matplotlib(mountains, out_dir):
	sorted_m = sorted(mountains, key=itemgetter(1), reverse=True)
	names = [m[0] for m in sorted_m]
	heights = [m[1] for m in sorted_m]

	plt.figure(figsize=(10, 6))
	bars = plt.bar(range(len(names)), heights, color='tab:blue')
	plt.xticks(range(len(names)), names, rotation=45, ha='right')
	plt.ylabel('Výška (m)')
	plt.title('Výšky vybraných hor')
	for rect, h in zip(bars, heights):
		plt.text(rect.get_x() + rect.get_width() / 2, h + 20, str(h), ha='center', va='bottom', fontsize=8)
	out_path = os.path.join(out_dir, 'mountains_bar.png')
	plt.tight_layout()
	plt.savefig(out_path)
	print(f'Uloženo: {out_path}')
	try:
		os.startfile(out_path)
	except Exception:
		pass
	try:
		plt.show()
	except Exception:
		pass

	heights = [m[1] for m in mountains]
	plt.figure(figsize=(8, 5))
	plt.hist(heights, bins=5, color='tab:green', edgecolor='black')
	plt.xlabel('Výška (m)')
	plt.ylabel('Počet hor')
	plt.title('Rozložení výšek')
	out_path2 = os.path.join(out_dir, 'mountains_hist.png')
	plt.tight_layout()
	plt.savefig(out_path2)
	print(f'Uloženo: {out_path2}')
	try:
		os.startfile(out_path2)
	except Exception:
		pass
	try:
		plt.show()
	except Exception:
		pass


def make_svg_bar(mountains, width=1000, height=500, margin=60):
	# mountains: list of (name, value)
	sorted_m = sorted(mountains, key=itemgetter(1), reverse=True)
	names = [m[0] for m in sorted_m]
	values = [m[1] for m in sorted_m]
	max_v = max(values) if values else 1

	n = len(values)
	chart_w = width - 2 * margin
	chart_h = height - 2 * margin
	bar_w = chart_w / max(n, 1) * 0.7
	gap = chart_w / max(n, 1) * 0.3

	svg_parts = [f'<svg width="{width}" height="{height}" viewBox="0 0 {width} {height}" xmlns="http://www.w3.org/2000/svg">']
	svg_parts.append(f'<rect width="100%" height="100%" fill="#fff"/>')
	# title
	svg_parts.append(f'<text x="{width/2}" y="30" text-anchor="middle" font-size="20">Výšky vybraných hor</text>')

	for i, (name, v) in enumerate(sorted_m):
		x = margin + i * (bar_w + gap) + gap/2
		bar_h = (v / max_v) * chart_h
		y = margin + (chart_h - bar_h)
		svg_parts.append(f'<rect x="{x:.1f}" y="{y:.1f}" width="{bar_w:.1f}" height="{bar_h:.1f}" fill="#2b7fb8">')
		svg_parts.append(f'<title>{name}: {v} m</title>')
		svg_parts.append('</rect>')
		# label
		svg_parts.append(f'<text x="{x + bar_w/2:.1f}" y="{height - margin/3:.1f}" text-anchor="middle" font-size="10">{name}</text>')
		# value above
		svg_parts.append(f'<text x="{x + bar_w/2:.1f}" y="{y - 5:.1f}" text-anchor="middle" font-size="10">{v}</text>')

	svg_parts.append('</svg>')
	return '\n'.join(svg_parts)


def make_svg_histogram(mountains, width=800, height=400, margin=50, bins=5):
	values = [m[1] for m in mountains]
	if not values:
		return '<svg></svg>'
	min_v = min(values)
	max_v = max(values)
	# compute bins
	bin_size = (max_v - min_v) / bins if max_v > min_v else 1
	counts = [0] * bins
	for v in values:
		idx = int((v - min_v) / bin_size) if bin_size > 0 else 0
		if idx == bins:
			idx = bins - 1
		counts[idx] += 1

	chart_w = width - 2 * margin
	chart_h = height - 2 * margin
	max_count = max(counts)
	bar_w = chart_w / bins * 0.8
	gap = chart_w / bins * 0.2

	svg = [f'<svg width="{width}" height="{height}" viewBox="0 0 {width} {height}" xmlns="http://www.w3.org/2000/svg">']
	svg.append(f'<rect width="100%" height="100%" fill="#fff"/>')
	svg.append(f'<text x="{width/2}" y="30" text-anchor="middle" font-size="18">Rozložení výšek (histogram)</text>')

	for i, c in enumerate(counts):
		x = margin + i * (bar_w + gap) + gap/2
		bar_h = (c / max_count) * chart_h if max_count > 0 else 0
		y = margin + (chart_h - bar_h)
		svg.append(f'<rect x="{x:.1f}" y="{y:.1f}" width="{bar_w:.1f}" height="{bar_h:.1f}" fill="#55a868">')
		svg.append(f'<title>Počet: {c}</title>')
		svg.append('</rect>')
		# x-label (range)
		lo = int(min_v + i * bin_size)
		hi = int(min_v + (i + 1) * bin_size)
		label = f"{lo}-{hi}"
		svg.append(f'<text x="{x + bar_w/2:.1f}" y="{height - margin/3:.1f}" text-anchor="middle" font-size="10">{label}</text>')
		# value above
		svg.append(f'<text x="{x + bar_w/2:.1f}" y="{y - 5:.1f}" text-anchor="middle" font-size="10">{c}</text>')

	svg.append('</svg>')
	return '\n'.join(svg)


def generate_html_report(mountains, out_dir):
	bar_svg = make_svg_bar(mountains)
	hist_svg = make_svg_histogram(mountains)
	html = f"""
<!doctype html>
<html lang="cs">
  <head>
	<meta charset="utf-8" />
	<title>Grafy hor</title>
	<style>
	  body {{ font-family: Arial, sans-serif; margin: 20px; background: #fafafa; color: #222 }}
	  .chart {{ margin-bottom: 30px; box-shadow: 0 2px 6px rgba(0,0,0,0.08); padding: 10px; background: #fff }}
	  h1 {{ font-size: 20px }}
	</style>
  </head>
  <body>
	<h1>Grafy výšek hor</h1>
	<div class="chart">{bar_svg}</div>
	<div class="chart">{hist_svg}</div>
	<p>Vygenerováno skriptem <code>bigData.py</code></p>
  </body>
</html>
"""

	out_path = Path(out_dir) / 'mountains_report.html'
	out_path.write_text(html, encoding='utf-8')
	print(f'Uloženo: {out_path}')
	try:
		webbrowser.open(out_path.as_uri())
	except Exception:
		pass


def main():
	try:
		base_dir = os.path.dirname(os.path.abspath(__file__))
	except NameError:
		base_dir = os.getcwd()

	mountains = get_sample_data()
	if HAS_MATPLOTLIB:
		plot_with_matplotlib(mountains, base_dir)
	else:
		print('matplotlib není nainstalován — generuji samostatný HTML report s vestavěnými SVG (žádná instalace není potřeba).')
		generate_html_report(mountains, base_dir)


if __name__ == '__main__':
	main()

