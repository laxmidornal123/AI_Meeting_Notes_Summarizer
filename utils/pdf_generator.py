from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

def generate_pdf(filename, transcript, summary):

    pdf = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    story = []

    story.append(Paragraph("<b>AI Meeting Notes Report</b>", styles["Title"]))

    story.append(Paragraph("<br/>", styles["Normal"]))

    story.append(Paragraph("<b>Transcript</b>", styles["Heading2"]))

    story.append(Paragraph(transcript, styles["BodyText"]))

    story.append(Paragraph("<br/>", styles["Normal"]))

    story.append(Paragraph("<b>AI Summary</b>", styles["Heading2"]))

    story.append(Paragraph(summary, styles["BodyText"]))

    pdf.build(story)