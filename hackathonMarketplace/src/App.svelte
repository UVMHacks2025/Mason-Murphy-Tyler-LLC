<script lang="ts">
	import SignUp from './SignUp.svelte';
	let isSignedUp = false;
	function handleSignUp() {
		isSignedUp = false;
	}
</script>

{#if !isSignedUp}
	<SignUp onSignUp={handleSignUp} />
{:else}
	<main>
		<header class="box1">
			<nav></nav>
			<h1>Welcome to Ridit</h1>
		</header>
		<section class="box2">
			<p> hello box 2</p>
		</section>
		<section class="box3">
			<p>Hello box3</p>
		</section>
		<section class="box4">
			<p>Hello World</p>
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
	.box1 {
		grid-row: 1;
		grid-column: 1;
	}
	.box2 {
		grid-row: 2/3;
		grid-column: 1;
	}
	.box3 {
		grid-row: 2;
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