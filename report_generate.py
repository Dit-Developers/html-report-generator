#   This Code is Developed by Muhammad Sudais Usmani 
#   Github: https://github.com/Dit-Developers/
#   LinkedIn: https://www.linkedin.com/in/muhammad-sudais-usmani-950889311/
#   Portfolio: https://msu-portfolio.vercel.app/


# ███╗   ███╗███████╗██╗   ██╗
# ████╗ ████║██╔════╝██║   ██║
# ██╔████╔██║███████╗██║   ██║
# ██║╚██╔╝██║╚════██║██║   ██║
# ██║ ╚═╝ ██║███████║╚██████╔╝
# ╚═╝     ╚═╝╚══════╝ ╚═════╝ 
#                Version 1.0.1

# Code Repository Link : https://github.com/Dit-Developers/html-report-generator/
from jinja2 import Template
import os
export_dir = "./Export"
files = os.listdir(export_dir)
exported_files = []
for file in files:
    ext = file.split(".")[-1].lower()
    file_path = os.path.join(export_dir, file)
    if ext in ["jpg", "png", "jpeg", "gif"]:
        exported_files.append({"type": "Image", "name": file, "path": file_path, "real_path": file_path})
    elif ext in ["pdf"]:
        exported_files.append({"type": "PDF", "name": file, "path": "https://cdn-icons-png.flaticon.com/512/337/337946.png", "real_path": file_path})
    elif ext in ["mp3", "wav", "aac"]:
        exported_files.append({"type": "Audio", "name": file, "path": "https://cdn-icons-png.flaticon.com/512/727/727245.png", "real_path": file_path})

# HTML Template for Exported Files Section
template_str = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Exported Files</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
    <div class="container my-5">
        <section class="mb-4">
            <h2>Exported Files</h2>
            <div class="row g-4">
                {% for file in exported_files %}
                <div class="col-12 col-sm-6 col-md-4 col-lg-3">
                    <div class="card border-0 shadow-sm">
                        <div class="card-img-top overflow-hidden" style="height: 200px; display: flex; justify-content: center; align-items: center; background-color: #f8f9fa;">
                            <img src="{{ file.path }}" alt="{{ file.type }} File" class="img-fluid h-100" style="object-fit: contain;">
                        </div>
                        <div class="card-body text-center">
                            <p class="card-text">{{ file.type }}: <a href="{{ file.real_path }}" target="_blank">{{ file.name }}</a></p>
                        </div>
                    </div>
                </div>
                {% endfor %}
            </div>
        </section>
    </div>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
"""

# Render HTML with Jinja2
template = Template(template_str)
output_html = template.render(exported_files=exported_files)

# Save the output HTML to a file
with open("Sudais_Usmani_Forensic_Report_PFTP_Assignment_CASE001.html", "w") as f:
    f.write(output_html)

print("HTML file generated: Sudais_Usmani_Forensic_Report_PFTP_Assignment_CASE001.html")
