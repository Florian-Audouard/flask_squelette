fetch("/getImg")
	.then((res) => {
		console.log(res);
		return res.json();
	})
	.then((data) => {
		document.querySelector(
			"#img_conteneur"
		).src = `data:image/jpg;base64, ${data.img_data}`;
	});
