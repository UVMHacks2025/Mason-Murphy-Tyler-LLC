<script lang="ts">
    import SignUp from './SignUp.svelte';
    let isSignedUp = false;
    
    function handleSignUp() {
        isSignedUp = true;
    }
	async function handleCreateListing(listing) {
		listing.preventDefault();
		const form = listing.target;
		const formData = new FormData(form);

		const response = await fetch ('http://localhost:5000/', {
			method: 'POST',
			body: formData
		});

		if (response.ok) {
			alert('Listing Successful');
		} else {
			alert('Failed to create listing')
		}
	}
</script>


{#if !isSignedUp}
    <SignUp on:signUp={handleSignUp} />
{:else}
	<main>
		<header class="box1">
			<h1>Welcome to Ridit!</h1>
			<img src="logo.png" alt="logo" class="logo">
		</header>
		<section class="box5">
			<form>
				<select name="category" id="category">
					<option value="furniture">Furniture</option>
					<option value="technology">Technology</option>
					<option value="outdoors">Outdoor Gear</option>
				</select>
				<input type="submit" value="Search">
			</form>
		</section>
		<section class="box2">
			<form action="#" method="POST">
				<h3>Make a Listing</h3>
				<button>
					Upload an Image
					<input type="file" name="image" required>
				</button>
				<button>
					Enter your item name:
					<input type="text" class="item" required>
				</button>
				<button>
					Which category does it belong in?
					<select name="category" id="category">
						<option value="furniture">Furniture</option>
						<option value="technology">Technology</option>
						<option value="outdoors">Outdoor Gear</option>
					</select>
				</button>
				<button>
					Enter your price:
					<input type="text" class="price" required>
				</button>
				<br>
				<input type="submit" value="Post Listing">
			</form>
		</section>
		<section class="box3">
			<div class="prod1">
				<!-- src will be image uploaded alt will be the prod name, h3 prod name, p price -->
				<img src = '/chair.jpg' alt="yes sir">
				<h3>Couch</h3>
				<p>$696969696969</p>
				
			</div>
			<div class="prod2">
				<!-- src will be image uploaded alt will be the prod name, h3 prod name, p price -->
				<img src = '/chair.jpg' alt="">
				<h3>Couch</h3>
				<p>$6969696969</p>
			</div>
			<div class="prod3">
				<!-- src will be image uploaded alt will be the prod name, h3 prod name, p price -->
				<img src = '/chair.jpg' alt="">
				<h3>Couch</h3>
				<p>$69696969696</p>
			</div>
		</section>
		<section class="box4">
			<div class="prod4">
				<!-- src will be image uploaded alt will be the prod name, h3 prod name, p price -->
				<img src = '/chair.jpg' alt="">
				<h3>Couch</h3>
				<p>$6969696969</p>
			</div>			
			<div class="prod5">
				<!-- src will be image uploaded alt will be the prod name, h3 prod name, p price -->
				<img src = '/chair.jpg' alt="">
				<h3>Couch</h3>
				<p>$6969696969</p>
			</div>			
			<div class="prod6">
				<!-- src will be image uploaded alt will be the prod name, h3 prod name, p price -->
				<img src = '/chair.jpg' alt="">
				<h3>Couch</h3>
				<p>$69696969</p>
			</div>
		</section>
		
	</main>

{/if}

<style>
	main {
		display: grid;
		grid-template-columns: auto auto auto auto;
		grid-template-rows: 10% auto auto auto;
		justify-content: space-evenly;
	}
	section {
		background-color: (0,0,0,.3);
		border-radius: .5em;
	}
	.box1 {
		margin: auto;
		grid-row: 1;
		grid-column: 1/2;
		justify-content: center;
		display: flex;
		
	}
	.box2 {
		grid-row: 2/3;
		grid-column: 1;
	}
	.box3 {
		grid-row: 2;
		display: flex;
		justify-content: space-evenly;
	}
	.box4 {
		grid-row: 3;
		grid-column: 2/4;
		display: flex;
		justify-content: space-evenly;
	}
	.box5 {
		grid-column: auto;
		grid-row: 1;
		justify-content: center;
		margin: auto
	}
	img {
		margin: auto;
		height: auto;
	}
	.logo{
		margin: auto;
		width:100px;
		height: 100px;
		grid-column: 1;
		
	}
	@media (min-width: 640px) {
		main {
			max-width: none;
		}
	}
</style>