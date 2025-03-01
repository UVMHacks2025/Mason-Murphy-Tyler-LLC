<script lang="ts">
    import SignUp from './SignUp.svelte';
    let isSignedUp = false;
	let showList = false;
    
	//handling the signup
    function handleSignUp() {
        isSignedUp = true;
    }
	/*
	// async function to post listing to the database
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
		*/
</script>


{#if !isSignedUp}
    <SignUp on:signUp={handleSignUp} />
{:else}
	<main>
		<header class="box1">
			<img src="logo.png" alt="logo" class="logo">
			<h1>RidIt</h1>
		</header>
		<section class="box5">
			<form>
				<select name="category" id="category">
					<option value="furniture">Furniture</option>
					<option value="technology">Technology</option>
					<option value="outdoors">Outdoor Gear</option>
				</select>
			</form>
		</section>
		<section class="box2">
			<form>
				<h3>Make a Listing</h3>
				<button>
					Enter your Email: 
					<input type="text" name="email" required>
				</button>
				<button>
					Enter your Password:
					<input type="text" name="password" required>
				</button>
				<button>
					Upload an Image
					<input type="file" name="image" required>
				</button>
				<button>
					Enter your item name:
					<input type="text" name="item" required>
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
					<input type="text" name="price" required>
				</button>
				<br>
				<input type="submit" value="Post Listing">
			</form>
		</section>
		<section class="box3">
			<div class="prod1">
				<!-- src will be image uploaded alt will be the prod name, h3 prod name, p price -->
				<img src = '/chair.jpg' alt="yes sir">
				<h3>Chair</h3>
				<p>$10</p>
				<button>Buy now <input type="button" ></button>
			</div>
			<div class="prod2">
				<!-- src will be image uploaded alt will be the prod name, h3 prod name, p price -->
				<img src = '/chair.jpg' alt="">
				<h3>Table</h3>
				<p>$10</p>
				<button>Buy now <input type="button"></button>
			</div>
			<div class="prod3">
				<!-- src will be image uploaded alt will be the prod name, h3 prod name, p price -->
				<img src = '/chair.jpg' alt="">
				<h3>Pillow</h3>
				<p>$15</p>
				<button>Buy now <input type="button"></button>
			</div>
		</section>
		<section class="box4">
			<div class="prod4">
				<!-- src will be image uploaded alt will be the prod name, h3 prod name, p price -->
				<img src = '/chair.jpg' alt="">
				<h3>Couch</h3>
				<p>$25</p>
				<button>Buy now <input type="button"></button>
			</div>			
			<div class="prod5">
				<!-- src will be image uploaded alt will be the prod name, h3 prod name, p price -->
				<img src = '/chair.jpg' alt="">
				<h3>Couch</h3>
				<p>$30</p>
				<button>Buy now <input type="button"></button>
			</div>			
			<div class="prod6">
				<!-- src will be image uploaded alt will be the prod name, h3 prod name, p price -->
				<img src = '/chair.jpg' alt="">
				<h3>Couch</h3>
				<p>$40</p>
				<button>Buy now <input type="button"></button>
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
		color: white;
	}
	section {
		background-color: rgba(0,0,0,.3);
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
	header > img {
		margin: auto;
		padding: 0em 4em;
		justify-content: space-around;
	}
	@media (min-width: 640px) {
		main {
			max-width: none;
		}
	}
</style>