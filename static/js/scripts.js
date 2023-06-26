fetch("/getImg")
	.then((res) => {
		return res.json();
	})
	.then((data) => {
		document.querySelector(
			"#img_conteneur"
		).src = `data:image/${data.type};base64, ${data.img_data}`;
	});
