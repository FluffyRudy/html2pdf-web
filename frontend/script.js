const textField = document.querySelector("textarea");
const submitBtn = document.querySelector("#submit");

async function getPDFData() {
    if (!textField.value) {
        alert("empty string");
        return;
    }
    const pdfData = textField.value;
    try {
        const response = await fetch("http://127.0.0.1:8000/api/createpdf/", {
            method: "POST",
            headers: {
                "Content-Type": "text/html",
            },
            body: pdfData,
        });
        if (response.status === 200) {
            const data = await response.blob();
            const url = URL.createObjectURL(data);

            const link = document.createElement("a");
            link.href = url;
            link.download = "document.pdf";
            document.body.appendChild(link);
            link.click();
        } else console.log(response.statusText);
    } catch (error) {
        console.error(error);
        alert(error.message);
    }
}

submitBtn.addEventListener("click", getPDFData);
document.addEventListener("DOMContentLoaded", () => {
    textField.addEventListener("keydown", function (e) {
        if (e.key == "Tab") {
            e.preventDefault();
            const start = this.selectionStart;
            const end = this.selectionEnd;

            this.value =
                this.value.substring(0, start) +
                "\t" +
                this.value.substring(end);

            this.selectionStart = this.selectionEnd = start + 1;
        }
    });
});
