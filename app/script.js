document.addEventListener("DOMContentLoaded", function () {
    const pic = document.getElementById("pic");
    const imageUpload = document.getElementById("image-upload");
    const predictButton = document.getElementById("predict-button");
    const predictedAge = document.getElementById("predicted-age");
    const predictedGender = document.getElementById("predicted-gender");
    const uploadedImage = document.getElementById("uploaded-image");
    
    // Event listener for the predict button
    predictButton.addEventListener("click", async function () {
        
        const fileInput = imageUpload.files[0];

        if (fileInput) {
            
            pic.src = URL.createObjectURL(fileInput);
            //image to show on webpage
            // uploadedImage.src = URL.createObjectURL(fileInput);
            
            // Create a FormData object to send the image file
            const formData = new FormData();
            formData.append("file", fileInput);

            try {
                // Send a POST request to your FastAPI backend
                const response = await fetch("http://127.0.0.1:8000/predict/", { method: "POST",body: formData});

                if (response.ok) {
                    // Parse the JSON response
                    const data = await response.json();
                
                    // Update the prediction result in the HTML
                    predictedAge.textContent =  data.age_group
                    predictedGender.textContent = data.gender;
                
                } else {
                    console.error("Error:", response.statusText);
                }
            } catch (error) {
                console.error("Error:", error);
            }

        } else 
            alert("Please select an image to predict.");
    });
});
