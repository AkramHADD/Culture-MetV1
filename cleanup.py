import os

file_path = "doc bus can.html"
with open(file_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

# Good parts:
# part 1: lines[0:116] (which is Index 0 to 115)
# part 2: lines[458:968] (which is Index 458 to 967)

part1 = "".join(lines[0:116])
part2 = "".join(lines[458:968])

html_template = """<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Documentation Technique - Banc d'essai Bus CAN/LIN</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: #f9fafb;
            color: #333;
            line-height: 1.6;
            margin: 0;
            padding: 0;
        }
        .page-container {
            max-width: 900px;
            margin: 40px auto;
            background: #fff;
            padding: 40px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            border-radius: 8px;
        }
        /* Cover Page Styles */
        .cover-page {
            text-align: center;
            padding: 80px 20px;
            border-bottom: 3px solid #004d99;
            margin-bottom: 50px;
            background: linear-gradient(135deg, #f0f4f8 0%, #d9e2ec 100%);
            border-radius: 8px;
        }
        .cover-page h1 {
            color: #004d99;
            font-size: 2.8em;
            margin-bottom: 10px;
        }
        .cover-page h2 {
            color: #4a5568;
            font-size: 1.6em;
            margin-bottom: 40px;
            font-weight: normal;
        }
        .cover-details {
            display: inline-block;
            text-align: left;
            background: #ffffff;
            padding: 30px 50px;
            border-radius: 8px;
            border-left: 6px solid #004d99;
            box-shadow: 0 4px 10px rgba(0,0,0,0.05);
            font-size: 1.2em;
        }
        .cover-details p {
            margin: 12px 0;
        }
        .group-members {
            margin-top: 20px;
            padding-top: 20px;
            border-top: 1px solid #e2e8f0;
            font-weight: bold;
            color: #2d3748;
        }
        
        /* Content Styles */
        h2 {
            color: #004d99;
            border-bottom: 2px solid #e2e8f0;
            padding-bottom: 8px;
            margin-top: 40px;
        }
        h3 {
            color: #2b6cb0;
            margin-top: 30px;
        }
        pre {
            background-color: #2d3748;
            color: #f7fafc;
            padding: 15px;
            border-radius: 5px;
            overflow-x: auto;
            font-family: 'Consolas', monospace;
        }
        
        /* Table Styles */
        table {
            width: 100%;
            border-collapse: collapse;
            margin: 25px 0;
            font-size: 0.95em;
            box-shadow: 0 0 20px rgba(0, 0, 0, 0.05);
            border-radius: 8px;
            overflow: hidden;
        }
        thead tr {
            background-color: #004d99;
            color: #ffffff;
            text-align: left;
        }
        th, td {
            padding: 15px 20px;
        }
        tbody tr {
            border-bottom: 1px solid #e2e8f0;
        }
        tbody tr:nth-of-type(even) {
            background-color: #f8fafc;
        }
        tbody tr:last-of-type {
            border-bottom: 2px solid #004d99;
        }
        tbody tr:hover {
            background-color: #edf2f7;
        }
    </style>
</head>
<body>
    <div class="page-container">
        <!-- Page de garde -->
        <div class="cover-page">
            <h1>Compte Rendu de Travaux Pratiques</h1>
            <h2>Banc d'essai Bus CAN/LIN - Audi A4 B7</h2>
            <div class="cover-details">
                <p><strong>Cours :</strong> Culture Métiers</p>
                <p><strong>Établissement :</strong> UFR Sciences et Technologies, Université Évry Paris-Saclay</p>
                <p><strong>Enseignant :</strong> Lamri NEHAOUA</p>
                <p><strong>Année universitaire :</strong> 2025-2026</p>
                <p><strong>Vitesse du bus :</strong> 100 kbit/s (réseau confort / habitacle)</p>
                <div class="group-members">
                    Groupe : Ismael ABOU ZEID, Wiame EL GHAMRI et Akram HADDOUCHE
                </div>
            </div>
        </div>
        
        <!-- Content starting from Section 1 -->
"""

html_footer = """
    </div>
</body>
</html>
"""

# Part 1 begins with "<h1>Documentation Technique...</h1>" and "<h2>1. Comprendre...</h2>"
# Let's cleanly stitch them. We'll remove the original h1 to avoid duplicates, as the cover page has a good title.
part1_cleaned = part1.replace("<h1>Documentation Technique - Banc d'essai Bus CAN/LIN</h1>", "")

with open(file_path, "w", encoding="utf-8") as f:
    f.write(html_template)
    f.write(part1_cleaned)
    f.write(part2)
    f.write(html_footer)

print("HTML structure rebuilt and styled.")
