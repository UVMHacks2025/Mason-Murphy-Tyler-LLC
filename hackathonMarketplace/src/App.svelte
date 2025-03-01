<script lang="ts">
	import SignUp from './SignUp.svelte';
	let isSignedUp = false;
	function handleSignUp() {
		isSignedUp = true;
	}
</script>

<!--
{#if !isSignedUp}
	<SignUp on:signUp={handleSignUp} />
{:else}
-->
	<main>
		<header class="box1">
			<nav></nav>
			<h1>Welcome to Ridit</h1>
		</header>
		<section class="box2">
		</section>
		<section class="box3">
			<div class="prod1">
				<!-- src will be image uploaded alt will be the prod name, h3 prod name, p price -->
				<img src = './assets/images/couch.jpg' alt="">
				<h3>Couch</h3>
				<p>$696969696969</p>
			</div>
			<div class="prod2">
				<!-- src will be image uploaded alt will be the prod name, h3 prod name, p price -->
				<img src = './assets/images/couch.jpg' alt="">
				<h3>Couch</h3>
				<p>$6969696969</p>
			</div>
			<div class="prod3">
				<!-- src will be image uploaded alt will be the prod name, h3 prod name, p price -->
				<img src = './assets/images/couch.jpg' alt="">
				<h3>Couch</h3>
				<p>$69696969696</p>
			</div>
		</section>
		<section class="box4">
			<div class="prod4">
				<!-- src will be image uploaded alt will be the prod name, h3 prod name, p price -->
				<img src = './assets/images/couch.jpg' alt="">
				<h3>Couch</h3>
				<p>$6969696969</p>
			</div>			
			<div class="prod5">
				<!-- src will be image uploaded alt will be the prod name, h3 prod name, p price -->
				<img src = './assets/images/couch.jpg' alt="">
				<h3>Couch</h3>
				<p>$6969696969</p>
			</div>			
			<div class="prod6">
				<!-- src will be image uploaded alt will be the prod name, h3 prod name, p price -->
				<img src = './assets/images/couch.jpg' alt="">
				<h3>Couch</h3>
				<p>$69696969</p>
			</div>
		</section>
		
	</main>

<!-- {/if} -->

<style>
	main {
		display: grid;
		grid-template-columns: auto auto auto auto;
		grid-template-rows: 10% auto auto auto;
		justify-content: space-evenly;
	}
	.box1 {
		margin: auto;
		grid-row: 1;
		grid-column: 1;
	}
	.box2 {
		grid-row: 2/3;
		grid-column: 1;
	}
	.box3 {
		grid-row: 2;
		display: flex;
		justify-content: center;
	}
	.box3 {
		grid-row: 3;
	}
	.box4 {
		grid-row: 4;
	}
	@media (min-width: 640px) {
		main {
			max-width: none;
		}
	}
</style>