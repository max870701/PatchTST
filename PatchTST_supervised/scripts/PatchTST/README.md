# Shell Script Input Parameters Explanation
1. `seq_len` is setting the length of the sequence that the model will look at each time step, also known as the context window.
2. `pre_len` is setting the length of the sequence that the model will predict.
3. `enc_in` is setting the number of input channels for the encoder.
4. `e_layers` is setting the number of layers for the encoder.
5. `n_heads` is setting the number of heads for the multi-head attention mechanism.
6. `d_model` is setting the dimensionality of the input and output for the model.
7. `d_ff` is setting the dimensionality of the feedforward network.
8. `dropout` is setting the dropout rate for the model.
9. `fc_dropout` is setting the dropout rate for the fully connected layer.
10. `head_dropout` is setting the dropout rate for the multi-head attention mechanism.
11. `patch_len` is setting the length of the patch.
12. `stride` is setting the stride of the patch.
13. `des 'Exp'` is setting the experiment name.
14. `train_epochs` is setting the number of epochs for training.
15. `lradj 'constant'` is setting the learning rate adjustment method.
16. `itr` is setting the number of iterations for training.
17. `batch_size` is setting the batch size for training.
18. `lr` is setting the learning rate for training.