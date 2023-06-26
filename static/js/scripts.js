fetch("/getImg")
	.then((res) => {
		return res.json();
	})
	.then((data) => {
		document.querySelector(
			"#img_conteneur"
		).src = `data:image/${data.type};base64, ${data.img_data}`;
	});
fetch("/getVideo")
	.then((res) => {
		console.log("ouep2");
		return res.json();
	})
	.then((data) => {
		const containeur = document.querySelector("#video_conteneur");
		const source = document.createElement("source");
		source.type = `video/${data.type}`;
		source.src = `data:video/${data.type};base64, ${data.video_data}`;
		containeur.appendChild(source);
	});
