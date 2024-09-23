<script charset="utf-8">
  let formText = '';
  let stuff = "nothing submitted yet";

  function handleSubmit() {
    stuff = formText;
  }
</script>

<form on:submit|preventDefault={handleSubmit}>
  <input bind:value={formText}/>
  <button type="submit">Submit</button>
</form>

<p>{ formText }</p>
<p>{ stuff }</p>
