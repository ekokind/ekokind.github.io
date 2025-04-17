---
layout: defaults/page
permalink: art.html
narrow: true
title: Art
---
<style>
.gallery {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
  grid-gap: 20px;
  margin: 20px 0;
}

.gallery-item {
  border: 1px solid #ddd;
  border-radius: 5px;
  padding: 10px;
  background-color: #fff;
  box-shadow: 0 2px 5px rgba(0,0,0,0.1);
  transition: transform 0.3s ease;
}

.gallery-item:hover {
  transform: translateY(-5px);
}

.gallery-image {
  width: 100%;
  height: 200px;
  object-fit: cover;
  border-radius: 3px;
  cursor: pointer;
}

.gallery-info {
  margin-top: 10px;
}

.gallery-title {
  font-weight: bold;
  font-size: 16px;
  margin: 5px 0;
}
  
.gallery-medium {
  color: #666;
  font-size: 14px;
  margin-bottom: 5px;
}
.gallery-date {
  color: #666;
  font-size: 14px;
  margin-bottom: 5px;
}

.gallery-status {
  display: inline-block;
  padding: 3px 8px;
  border-radius: 3px;
  font-size: 12px;
  font-weight: bold;
}

.for-sale {
  background-color: #e6f7e6;
  color: #2e8b57;
}

.not-for-sale {
  background-color: #f7e6e6;
  color: #8b2e2e;
}

/* Modal styles for enlarged image view */
.modal {
  display: none;
  position: fixed;
  z-index: 1000;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0,0,0,0.8);
}
.modal-content {
  margin: auto;
  display: block;
  max-width: 90%;
  max-height: 80vh;
  object-fit: contain; /* This preserves aspect ratio */
  cursor: default; /* Keep default cursor over the image */
}

.modal-caption {
  color: white;
  text-align: center;
  padding: 10px;
  width: 80%;
  margin: auto;
}

.close {
  position: absolute;
  top: 15px;
  right: 35px;
  color: #f1f1f1;
  font-size: 40px;
  font-weight: bold;
  transition: 0.3s;
  cursor: pointer;
  z-index: 1001; /* Ensure close button is above other elements */
}

.close:hover {
  color: #bbb;
}

/* Add instructions text */
.modal-instructions {
  position: absolute;
  bottom: 20px;
  left: 0;
  width: 100%;
  color: #ccc;
  font-size: 14px;
  text-align: center;
}

.close:hover {
  color: #bbb;
}

@media only screen and (max-width: 700px) {
  .modal-content {
    width: 100%;
  }
}
</style>

<div class="gallery">
  <!-- Art Item 1 -->
  <div class="gallery-item">
    <img src="theme/img/artsfest_2023-1.jpg" alt="Rainbow Corals" class="gallery-image" onclick="openModal(this)">
    <div class="gallery-info">
      <h3 class="gallery-title">Rainbow Corals</h3>
      <p class="gallery-date">2023</p>
      <span class="gallery-status for-sale">Sold</span>
    </div>
  </div>

  <div class="gallery-item">
    <img src="theme/img/purpcoral.jpg" alt="Purple Coral" class="gallery-image" onclick="openModal(this)">
    <div class="gallery-info">
      <h3 class="gallery-title">PurpleCoral_01</h3>
      <p class="gallery-medium">wool, beading, cotton embroidery</p>
      <p class="gallery-date">January 2024</p>
      <span class="gallery-status not-for-sale">$125</span>
    </div>
  </div>
  
  <!-- Add more art items as needed -->
</div>

<!-- Modal for enlarged images -->
<div id="imageModal" class="modal">
  <span class="close" onclick="closeModal()">&times;</span>
  <img class="modal-content" id="enlargedImage">
  <div id="caption" class="modal-caption"></div>
</div>

<script>
function openModal(img) {
  var modal = document.getElementById("imageModal");
  var modalImg = document.getElementById("enlargedImage");
  var captionText = document.getElementById("caption");
  
  modal.style.display = "block";
  modalImg.src = img.src;
  captionText.innerHTML = img.alt;
}

function closeModal() {
  document.getElementById("imageModal").style.display = "none";
}

// Close the modal when clicking outside the image
window.onclick = function(event) {
  var modal = document.getElementById("imageModal");
  if (event.target == modal) {
    modal.style.display = "none";
  }
};
  
// Close the modal when hitting esc key
document.addEventListener('keydown', function(event) {
  if (event.key === 'Escape') {
    closeModal();
  }
});
</script>
