from js import document, console

# Simple club descriptions (currently the club name; you can expand these later)
club_descriptions = {
	"Dance Club": "Our dance club brings people together through rhythm and collaboration. Whether you’re here to learn, perform, or just enjoy the energy, it’s a place where everyone belongs.",
	"Math Club": "Our math club is a space for problem‑solvers to sharpen skills, share ideas, and explore concepts beyond the classroom. We focus on collaboration, critical thinking, and applying mathematics to real‑world challenges.",
	"Science Club": "Our science club is a space to explore ideas beyond the classroom. We focus on inquiry, experimentation, and discussion, encouraging members to connect theory with real‑world applications.",
}


def show_club_description(*args, **kwargs):
	
    
	try:
		club_select = document.getElementById("club-select")
		if club_select is None:
			console.log("club-select element not found")
			return

		selected_club = club_select.value
		desc_area = document.getElementById("description-area")
		if desc_area is None:
			console.log("description-area element not found")
			return

		if selected_club and selected_club in club_descriptions:
			# show club name (you can replace this with full description text)
			desc_html = f"<h3 style='color: white;'>{club_descriptions[selected_club]}</h3>"
		else:
			desc_html = "<p style='color: white;'>Please select a club first.</p>"

		desc_area.innerHTML = desc_html
	except Exception as e:
		console.log("Error in show_club_description:", e)

